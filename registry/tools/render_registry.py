import json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open("E:/AI Programs/Toolchain/registry/mechanisms.json", encoding="utf-8"))["mechanisms"]
head = open(os.path.join(HERE, "registry_head.md"), encoding="utf-8").read()
S = {"built": "B", "documented-only": "D", "planned": "P"}
SC = {"universal": "U", "pirate-specific": "P", "mixed": "M"}
def cell(s): return str(s).replace("|", "/").replace("\n", " ")
engines = ["reality", "life", "kernel", "settlement", "economy", "cognition", "society", "government", "knowledge", "history", "catalogue", "shared", "pirate-ship"]
summ = []
for e in engines:
    c = collections.Counter(r["status"] for r in d if r["owning_engine"] == e and r["kind"] == "mechanism")
    summ.append(f"| {e} mechanisms | {c['built']} | {c['documented-only']} | {c['planned']} | {sum(c.values())} |")
c = collections.Counter(r["status"] for r in d if r["kind"] == "restatement")
summ.append(f"| restatements (pirate docs and adapters) | {c['built']} | {c['documented-only']} | {c['planned']} | {sum(c.values())} |")
c = collections.Counter(r["status"] for r in d)
summ.append(f"| **all rows** | {c['built']} | {c['documented-only']} | {c['planned']} | {len(d)} |")
_ng = len(json.load(open("E:/AI Programs/Toolchain/registry/graph.json", encoding="utf-8"))["overlap_groups"])
out = [head.replace("__SUMMARY__", "\n".join(summ)).replace("__NGROUPS__", str(_ng))]
for e in engines:
    rows = [r for r in d if r["owning_engine"] == e and r["kind"] == "mechanism"]
    out.append(f"\n### {e} ({len(rows)})\n\n| id | st | dom | sc | ev | V&V | overlaps | home |\n|---|---|---|---|---|---|---|---|")
    for r in rows:
        ov = " ".join(r["overlap_groups"] + r["unit_issues"])
        home = r["home"].replace("Games/RPG's/pirate-ship/files/pirate-ship/", "ps/").replace("Toolchain/", "")
        vv = r.get("vv", {})
        vvs = ("I" if vv.get("implemented") else "-") + ("T" if vv.get("record", {}).get("integration_tested_with") else "-") + ("V" if str(vv.get("validated", "")).startswith("yes") else ("v" if str(vv.get("validated", "")).startswith("candidate") else ("F" if str(vv.get("validated", "")).startswith("failed") else "-")))
        out.append(f"| `{r['id']}` | {S[r['status']]} | {r['domain']} | {SC[r['scope']]} | {r['evidence'] or '?'} | {vvs} | {ov} | {cell(home)[:90]} |")
rows = [r for r in d if r["kind"] == "restatement"]
out.append(f"\n## Restatements ({len(rows)}): docs and adapters that restate an owned mechanism\n\n"
           "Each points at its owner. Edit the owner, never the restatement's formula; the doc should cite the owner's id.\n\n"
           "| restatement | restates (owner) | overlaps | home |\n|---|---|---|---|")
for r in rows:
    home = r["home"].replace("Games/RPG's/pirate-ship/files/pirate-ship/", "ps/").replace("Toolchain/", "")
    out.append(f"| `{r['id']}` | `{r['restates']}` | {' '.join(r['overlap_groups'] + r['unit_issues'])} | {cell(home)[:80]} |")
out.append("\n`ps/` = `Games/RPG's/pirate-ship/files/pirate-ship/`. Engine paths are under `Toolchain/`.\n\n"
           "## Maintaining the registry (proposed)\n\n"
           "- A new mechanism gets a row before its code or doc: id, owner, the §7 fields. Its author searches first.\n"
           "- A keeper whose change adds, moves or removes a mechanism updates its row in the same turn and tells the registry keeper.\n"
           "- Overlap groups close only when Rex approves an owner and the losing homes become restatements or reads.\n"
           "- The registry keeper re-audits after each phase of ROADMAP.md.\n")
open("E:/AI Programs/Toolchain/REGISTRY.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len("\n".join(out)))
