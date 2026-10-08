// Render SVGs to PNG previews (and optionally a print PDF) with Chromium.
// usage: node render.mjs <out_dir> <file.svg>...      -> PNG previews
//        node render.mjs --pdf <out.pdf> <file.svg>... -> one 8.5x11 PDF
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import { readFileSync, writeFileSync } from 'fs';
import { basename, join } from 'path';

const args = process.argv.slice(2);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage();

if (args[0] === '--pdf') {
  const out = args[1];
  const files = args.slice(2);
  const body = files.map(f => {
    const svg = readFileSync(f, 'utf8').replace(/<\?xml[^>]*>/, '');
    return `<div class="pg">${svg}</div>`;
  }).join('');
  await page.setContent(`<!doctype html><html><head><style>
    @page { size: 8.5in 11in; margin: 0 }
    body { margin: 0 } .pg { width: 8.5in; height: 11in; page-break-after: always; overflow: hidden }
    .pg svg { display: block; width: 8.5in; height: 11in }
  </style></head><body>${body}</body></html>`);
  await page.pdf({ path: out, width: '8.5in', height: '11in', printBackground: true });
} else {
  const outDir = args[0];
  for (const f of args.slice(1)) {
    const svg = readFileSync(f, 'utf8');
    const m = svg.match(/viewBox="0 0 (\d+) (\d+)"/);
    const w = +m[1], h = +m[2];
    const scale = 1.6;
    await page.setViewportSize({ width: Math.round(w * scale), height: Math.round(h * scale) });
    await page.setContent(`<!doctype html><html><body style="margin:0;background:#fff">
      <img src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}" style="width:${w * scale}px;height:${h * scale}px;display:block"></body></html>`);
    await page.waitForTimeout(150);
    const out = join(outDir, basename(f).replace(/\.svg$/, '.png'));
    await page.screenshot({ path: out });
    console.log('wrote', out);
  }
}
await browser.close();
