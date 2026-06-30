import { chromium } from 'playwright';

const htmlPath = '/Users/zuo/Desktop/社媒/FB/W1/v2/skip-middlemen.html';
const pngPath = '/Users/zuo/Desktop/社媒/FB/W1/v2/skip-middlemen.png';

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2 });
await page.setViewportSize({ width: 1080, height: 1080 });

const logs = [];
page.on('console', msg => logs.push(`[${msg.type()}] ${msg.text()}`));
page.on('pageerror', err => logs.push(`[PAGE_ERROR] ${err.message}`));

await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

// Font load check
const fontsLoaded = await page.evaluate(() => {
  const fonts = [...document.fonts];
  return {
    bebasNeue: fonts.some(f => f.family === 'Bebas Neue' && f.status === 'loaded'),
    outfit: fonts.some(f => f.family === 'Outfit' && f.status === 'loaded'),
    dmSans: fonts.some(f => f.family === 'DM Sans' && f.status === 'loaded'),
  };
});
console.log('Fonts loaded:', JSON.stringify(fontsLoaded));

// Layout verification
const checks = await page.evaluate(() => {
  const body = document.body;
  const headline = document.querySelector('.headline');
  const flow = document.querySelector('.flow');
  const brand = document.querySelector('.brand');
  return {
    bodySize: { w: body.offsetWidth, h: body.offsetHeight },
    headlineFont: headline ? window.getComputedStyle(headline).fontSize : 'N/A',
    flowWidth: flow ? flow.offsetWidth : 'N/A',
    brandColor: brand ? window.getComputedStyle(brand).color : 'N/A',
    brandFontWeight: brand ? window.getComputedStyle(brand).fontWeight : 'N/A',
  };
});
console.log('Layout check:', JSON.stringify(checks, null, 2));

if (logs.length) console.log('Console logs:\n' + logs.join('\n'));

await page.screenshot({ path: pngPath, type: 'png' });
console.log(`Rendered: ${pngPath}`);
await browser.close();
