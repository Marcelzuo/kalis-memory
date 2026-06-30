const { chromium } = require('playwright');
const path = require('path');

const slides = [
  { html: 'slide-1.html', png: 'slide-1.png' },
  { html: 'slide-2.html', png: 'slide-2.png' },
  { html: 'slide-3.html', png: 'slide-3.png' },
  { html: 'slide-4.html', png: 'slide-4.png' },
  { html: 'slide-5.html', png: 'slide-5.png' },
];

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1080, height: 1080 },
    deviceScaleFactor: 2,
  });

  for (const slide of slides) {
    const page = await context.newPage();
    const filePath = 'file://' + path.resolve(slide.html);
    await page.goto(filePath, { waitUntil: 'networkidle' });
    // Ensure fonts are loaded
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({
      path: slide.png,
      fullPage: false,
    });
    console.log('✓', slide.png);
    await page.close();
  }

  await browser.close();
  console.log('Done — 5 slides rendered');
})();
