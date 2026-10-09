// Cover QC: bounding boxes of the key groups vs the 0.375 in safe area.
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import { readFileSync } from 'fs';
const svg = readFileSync(process.argv[2], 'utf8');
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage();
await page.setContent(`<!doctype html><body style="margin:0">${svg}</body>`);
const r = await page.evaluate(() => {
  const out = {};
  for (const id of ['type', 'badge', 'characters', 'dot-hidden', 'series-border', 'scenery']) {
    const b = document.getElementById(id).getBBox();
    out[id] = [b.x, b.y, b.x + b.width, b.y + b.height].map(v => +v.toFixed(1));
  }
  return out;
});
const SAFE = 27, W = 612, H = 792;
for (const [k, [x0, y0, x1, y1]] of Object.entries(r)) {
  const ok = x0 >= SAFE && y0 >= SAFE && x1 <= W - SAFE && y1 <= H - SAFE;
  console.log(k.padEnd(14), [x0, y0, x1, y1].join(', '), ok ? 'inside safe area' : '(extends past 0.375 in)');
}
await browser.close();
