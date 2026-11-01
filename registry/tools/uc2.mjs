import { parse } from 'file:///E:/AI%20Programs/Toolchain/kernel/src/units.ts';
import fs from 'node:fs';
const p = 'E:/AI Programs/Toolchain/registry/quantities.json';
const doc = JSON.parse(fs.readFileSync(p, 'utf8'));
const tally = {};
for (const x of doc.quantities) {
  if (x.kind && x.kind !== 'quantity') { x.unit_parses = null; const k = 'kind ' + x.kind; tally[k] = (tally[k] || 0) + 1; continue; }
  if (x.unit != null) {
    try { parse(String(x.unit)); x.unit_parses = true; if (String(x.unit_status).startsWith('needs')) x.unit_status = 'mapped (symbol added by kernel 2648)'; } catch (e) { x.unit_parses = false; x.unit_error = String(e.message); if (!String(x.unit_status).startsWith('needs')) x.unit_status = 'fails the kernel parser: ' + x.unit_error; }
  } else x.unit_parses = false;
  const k = x.unit_parses ? 'parses' : String(x.unit_status).split(' ')[0] + ' ' + (String(x.unit_status).split(' ')[1] || '');
  tally[k] = (tally[k] || 0) + 1;
}
doc.meta.unit_check = { checked: '2026-10-30', parser: 'Toolchain/kernel/src/units.ts parse (unit 2592)', tally };
fs.writeFileSync(p, JSON.stringify(doc, null, 1));
console.log(tally);
for (const x of doc.quantities) if (!x.unit_parses && String(x.unit_status).startsWith('fails')) console.log(' ', x.id, x.unit, x.unit_text);
const need = new Set(doc.quantities.filter(x => String(x.unit_status).startsWith('needs')).map(x => x.unit)); console.log('needs', [...need].join(', '));
