const puppeteer = require('puppeteer-core');
const path = require('path');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const HTML_PATH = 'file://' + path.resolve(__dirname, 'index.html');

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 1000 });
  await page.goto(HTML_PATH, { waitUntil: 'networkidle0' });

  const mode = process.argv[2] || 'screenshot';

  if (mode === 'screenshot') {
    const selector = process.argv[3]; // optional: CSS selector to screenshot just one element
    if (selector) {
      const el = await page.$(selector);
      await el.screenshot({ path: path.resolve(__dirname, 'preview.png') });
    } else {
      await page.screenshot({ path: path.resolve(__dirname, 'preview.png'), fullPage: true });
    }
    console.log('Wrote preview.png');
  } else if (mode === 'pdf') {
    await page.emulateMediaType('print');
    await page.pdf({
      path: path.resolve(__dirname, 'How to Start a Startup.pdf'),
      format: 'Letter',
      printBackground: true,
      margin: { top: '0.6in', bottom: '0.6in', left: '0.6in', right: '0.6in' },
    });
    console.log('Wrote PDF');
  }

  await browser.close();
})();
