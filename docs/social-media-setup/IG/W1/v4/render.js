const { chromium } = require('playwright');
const path = require('path');

const OUT = __dirname;

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1080, height: 1080 });

  const htmlPath = 'file://' + path.resolve(OUT, 'slides.html');
  await page.goto(htmlPath, { waitUntil: 'networkidle' });

  // Ensure fonts are rendered
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(1500);

  for (let i = 1; i <= 5; i++) {
    const el = await page.$(`#s${i}`);
    if (!el) {
      console.error(`[ERROR] Element #s${i} not found`);
      continue;
    }
    const outPath = path.join(OUT, `s${i}.png`);
    await el.screenshot({ path: outPath, type: 'png' });
    console.log(`[OK] s${i}.png saved`);
  }

  await browser.close();
  console.log('[DONE] All 5 slides rendered.');
})();
