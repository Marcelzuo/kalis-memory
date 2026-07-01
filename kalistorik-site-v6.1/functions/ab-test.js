/**
 * Cloudflare Worker — A/B Testing with GA4 variant tracking
 *
 * ── USAGE ──────────────────────────────────────────────────
 * 1. Deploy to Cloudflare Workers: `wrangler deploy functions/ab-test.js`
 * 2. Add a Worker Route in CF Dashboard: `kalistorik.com/*` → this worker
 * 3. Create two deployment variants:
 *    - Variant A: your main deployment (e.g., production)
 *    - Variant B: your experiment deployment (e.g., ab-test branch)
 * 4. The worker randomly assigns each visitor to A or B via a cookie,
 *    then proxies to the correct origin. GA4 `ab_test_variant` event fires.
 *
 * ── CUSTOMISATION ─────────────────────────────────────────
 * - ORIGIN_A / ORIGIN_B: the two variant backends
 * - COOKIE_TTL_DAYS: how long the cookie persists
 * - TRAFFIC_SPLIT: percentage sent to variant B (0–1)
 * - GA4_MEASUREMENT_ID: your GA4 property
 *
 * ── HOW IT WORKS ──────────────────────────────────────────
 * 1. Check for existing `ab_variant` cookie → if found, use that variant
 * 2. No cookie → random roll weighted by TRAFFIC_SPLIT → set cookie
 * 3. Proxy request to the selected origin
 * 4. Inject GA4 `ab_test_variant` event snippet into HTML responses
 */

const ORIGIN_A = 'https://kalistorik.com';       // control
const ORIGIN_B = 'https://ab.kalistorik.com';     // variant B (configure this)
const COOKIE_NAME = 'ab_variant';
const COOKIE_TTL_DAYS = 30;
const TRAFFIC_SPLIT = 0.5;                        // 50% to variant B
const GA4_MEASUREMENT_ID = 'G-YRPEYWWLM1';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const cookieHeader = request.headers.get('Cookie') || '';

    // ── Step 1: Determine variant ──
    let variant = getCookie(cookieHeader, COOKIE_NAME);

    if (!variant) {
      // Random assignment
      variant = Math.random() < TRAFFIC_SPLIT ? 'B' : 'A';
    }

    // ── Step 2: Route to origin ──
    const origin = variant === 'B' ? ORIGIN_B : ORIGIN_A;
    const targetUrl = origin + url.pathname + url.search;

    // Clone request with cleaned headers (strip cookie for origin)
    const headers = new Headers(request.headers);
    headers.set('X-AB-Variant', variant);

    const originResponse = await fetch(targetUrl, {
      method: request.method,
      headers: headers,
      body: request.body,
      redirect: 'manual',
    });

    // ── Step 3: Inject GA4 event snippet into HTML ──
    const contentType = originResponse.headers.get('Content-Type') || '';
    let response;

    if (contentType.includes('text/html')) {
      const body = await originResponse.text();
      const injected = injectGA4Variant(body, variant);
      response = new Response(injected, originResponse);
    } else {
      response = new Response(originResponse.body, originResponse);
    }

    // ── Step 4: Set variant cookie ──
    response.headers.set(
      'Set-Cookie',
      `${COOKIE_NAME}=${variant}; Path=/; Max-Age=${COOKIE_TTL_DAYS * 86400}; SameSite=Lax; Secure`
    );

    return response;
  },
};

/**
 * Parse a cookie value by name.
 */
function getCookie(cookieHeader, name) {
  const match = cookieHeader.match(new RegExp(`(?:^|;\\s*)${name}=([^;]*)`));
  return match ? match[1] : null;
}

/**
 * Inject GA4 `ab_test_variant` event before </head>.
 */
function injectGA4Variant(html, variant) {
  const snippet = `<script>if(typeof gtag==='function'){gtag('event','ab_test_variant',{variant:'${variant}'});}</script>`;
  return html.replace('</head>', snippet + '\n</head>');
}
