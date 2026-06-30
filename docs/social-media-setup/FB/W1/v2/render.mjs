import { chromium } from 'playwright';

const htmlPath = '/Users/zuo/Desktop/社媒/FB/W1/v2/supply-truth.html';
const pngPath = '/Users/zuo/Desktop/社媒/FB/W1/v2/supply-truth.png';

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2 });
await page.setViewportSize({ width: 1080, height: 1080 });

const logs = [];
page.on('console', msg => logs.push(`[${msg.type()}] ${msg.text()}`));
page.on('pageerror', err => logs.push(`[PAGE_ERROR] ${err.message}`));

await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

// Check editorial fonts loaded
const fontsLoaded = await page.evaluate(() => {
  const fonts = [...document.fonts];
  const cg = fonts.some(f => f.family === 'Cormorant Garamond' && f.status === 'loaded');
  const pd = fonts.some(f => f.family === 'Playfair Display' && f.status === 'loaded');
  return { cormorantGaramond: cg, playfairDisplay: pd };
});
console.log('Fonts loaded:', JSON.stringify(fontsLoaded));

// Layout verification
const checks = await page.evaluate(() => {
  const body = document.body;
  const quote = document.querySelector('.quote');
  const footer = document.querySelector('.footer');
  const brand = document.querySelector('.brand');
  const tagline = document.querySelector('.tagline');
  return {
    bodySize: { w: body.offsetWidth, h: body.offsetHeight },
    quoteText: quote?.textContent?.trim().slice(0, 60),
    quoteFontSize: quote ? window.getComputedStyle(quote).fontSize : 'N/A',
    brandColor: brand ? window.getComputedStyle(brand).color : 'N/A',
    taglineColor: tagline ? window.getComputedStyle(tagline).color : 'N/A',
    brandFontWeight: brand ? window.getComputedStyle(brand).fontWeight : 'N/A',
    footerBottom: footer ? window.getComputedStyle(footer).bottom : 'N/A',
  };
});
console.log('Layout check:', JSON.stringify(checks, null, 2));

if (logs.length) console.log('Console logs:\n' + logs.join('\n'));

await page.screenshot({ path: pngPath, type: 'png' });
console.log(`Rendered: ${pngPath}`);
await browser.close();
