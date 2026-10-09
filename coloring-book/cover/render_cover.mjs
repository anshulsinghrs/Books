// Render the cover SVG to PNG at a given pixel width (default: 300 DPI from the viewBox, 2550 px for 8.5 in).
// usage: node render_cover.mjs <in.svg> <out.png> [width_px]
//        node render_cover.mjs --pdf <in.svg> <out.pdf>   (vector PDF at the SVG's physical size)
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import { readFileSync } from 'fs';
const args = process.argv.slice(2);
const pdf = args[0] === '--pdf'; if (pdf) args.shift();
const [inp, out, wArg] = args;
const vb = readFileSync(inp, 'utf8').match(/viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"/);
const w = +(wArg || Math.round(vb[3] / 72 * 300)), h = Math.round(w * vb[4] / vb[3]);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: w, height: h } });
const svg = readFileSync(inp);
await page.setContent(`<!doctype html><html><head><style>@page{margin:0}</style></head><body style="margin:0"><img src="data:image/svg+xml;base64,${svg.toString('base64')}" style="${pdf ? `width:${vb[3] / 72}in;height:${vb[4] / 72}in` : `width:${w}px;height:${h}px`};display:block"></body></html>`);
await page.waitForTimeout(800);
if (pdf) {
  const [, , vw, vh] = vb.slice(1).map(Number);
  await page.pdf({ path: out, width: `${vw / 72}in`, height: `${vh / 72}in`, printBackground: true, pageRanges: '1' });
} else {
  await page.screenshot({ path: out });
}
await browser.close();
console.log('wrote', out, w + 'x' + h);
