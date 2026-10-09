// Render the cover SVG to PNG at a given pixel width (default: 300 DPI from the viewBox, 2550 px for 8.5 in).
// usage: node render_cover.mjs <in.svg> <out.png> [width_px]
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import { readFileSync } from 'fs';
const [inp, out, wArg] = process.argv.slice(2);
const vb = readFileSync(inp, 'utf8').match(/viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"/);
const w = +(wArg || Math.round(vb[3] / 72 * 300)), h = Math.round(w * vb[4] / vb[3]);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ viewport: { width: w, height: h } });
const svg = readFileSync(inp);
await page.setContent(`<!doctype html><html><body style="margin:0"><img src="data:image/svg+xml;base64,${svg.toString('base64')}" style="width:${w}px;height:${h}px;display:block"></body></html>`);
await page.waitForTimeout(800);
await page.screenshot({ path: out });
await browser.close();
console.log('wrote', out, w + 'x' + h);
