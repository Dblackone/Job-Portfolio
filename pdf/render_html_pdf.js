const fs = require('fs');
const process = require('process');
const { chromium } = require(process.env.FORGE_NODE_PATH + '\\playwright');

const [htmlPath, outputPath] = process.argv.slice(2);
if (!htmlPath || !outputPath) {
  throw new Error('Usage: node render_html_pdf.js <html> <output.pdf>');
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage();
    await page.setContent(fs.readFileSync(htmlPath, 'utf8'), { waitUntil: 'networkidle' });
    await page.pdf({
      path: outputPath,
      format: 'A4',
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: '0', right: '0', bottom: '0', left: '0' },
    });
  } finally {
    await browser.close();
  }
})();
