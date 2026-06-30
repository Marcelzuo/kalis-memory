import { chromium } from 'playwright';

const htmlPath = '/Users/zuo/Desktop/社媒/FB/W1/v1/cost-chain.html';
const pngPath = '/Users/zuo/Desktop/社媒/FB/W1/v1/cost-chain.png';

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2 });
await page.setViewportSize({ width: 1080, height: 1080 });

// Capture console
const logs = [];
page.on('console', msg => logs.push(`[${msg.type()}] ${msg.text()}`));
page.on('pageerror', err => logs.push(`[PAGE_ERROR] ${err.message}`));

await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

// Check if Montserrat loaded
const fontLoaded = await page.evaluate(() => {
  const fonts = [...document.fonts];
  return fonts.some(f => f.family === 'Montserrat' && f.status === 'loaded');
});
console.log('Montserrat loaded:', fontLoaded);

// Check key element positions
const checks = await page.evaluate(() => {
  const body = document.body;
  const cards = [...document.querySelectorAll('.cost-card')];
  const footer = document.querySelector('.footer');
  const brand = document.querySelector('.brand');
  return {
    bodySize: { w: body.offsetWidth, h: body.offsetHeight },
    cardCount: cards.length,
    card5Price: cards[4]?.querySelector('.price')?.textContent,
    footerBottom: footer ? window.getComputedStyle(footer).bottom : 'N/A',
    brandFontSize: brand ? window.getComputedStyle(brand).fontSize : 'N/A',
    brandLetterSpacing: brand ? window.getComputedStyle(brand).letterSpacing : 'N/A',
    brandFontWeight: brand ? window.getComputedStyle(brand).fontWeight : 'N/A',
  };
});
console.log('Layout check:', JSON.stringify(checks, null, 2));

if (logs.length) console.log('Console logs:', logs.join('\n'));

await page.screenshot({ path: pngPath, type: 'png' });
console.log(`Rendered: ${pngPath}`);
await browser.close();
