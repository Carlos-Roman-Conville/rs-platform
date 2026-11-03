"""Lint INTEGRATION-PLAN.md: one active row per contract id (REG-42).

Usage: plan_lint.py PLAN.md | plan_lint.py --selftest
Standard library only; reads the plan, never edits it.
"""
import re
import sys

ID_RE = re.compile(r"^(M1a|M1b|M2|M3|M4|M5)-\d+[a-z]?$|^(INH|INV|DC|NP|RC|U)-\d+$")
CITE_RE = re.compile(r"(?<![A-Za-z-])(M1a|M1b|M2|M3|M4|M5)-\d+[a-z]?(?![A-Za-z0-9])")
M1A_TWO_DIGIT = re.compile(r"^M1a-\d\d[a-z]?$")
REGISTER_HEAD = re.compile(r"^\|\s*Contract\s*\|\s*Rev\s*\|")


def lint(text):
    """Return (exit_code, output lines)."""
    rows = {}
    cited = {}
    in_log = False
    in_register = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            in_log = line.strip().lower() == "## log"
            in_register = False
        if in_log:
            continue
        for m in CITE_RE.finditer(line):
            cited.setdefault(m.group(0), []).append(n)
        if not line.lstrip().startswith("|"):
            in_register = False
            continue
        if REGISTER_HEAD.match(line):
            in_register = True
            continue
        if in_register:
            continue
        cid = line.strip().strip("|").split("|")[0].replace("**", "").strip()
        if ID_RE.match(cid):
            rows.setdefault(cid, []).append(n)

    out, fail = [], False
    for cid, lines in sorted(rows.items()):
        if len(lines) > 1:
            fail = True
            out.append("duplicate %s: rows at lines %s" % (cid, ", ".join(map(str, lines))))
    for cid, lines in sorted(cited.items()):
        if cid in rows:
            continue
        where = ", ".join(map(str, lines[:8]))
        if M1A_TWO_DIGIT.match(cid):
            fail = True
            out.append("undefined %s: cited at lines %s but defines no row" % (cid, where))
        else:
            out.append("warning: %s cited at lines %s but defines no row" % (cid, where))
    if not fail:
        out.append("plan-lint: %d contract rows, 0 duplicates" % len(rows))
    return (1 if fail else 0), out


def selftest():
    clean = "## 2. M1a\n| ID | x |\n|---|---|\n| **M1a-10** | a |\n| M1a-11 | b |\n"
    dup = clean + "| M1a-10 | old |\n"
    register = ("| M1a-10 | def |\n\n## 2e\n| Contract | Rev | Agreed |\n|---|---|---|\n| M1a-10 | 2 | y |\n"
                "| M1a-10 | 3 | y |\n\n## Log\n| M1a-10 | old |\n")
    for name, text, want in (("clean", clean, 0), ("dup", dup, 1), ("register", register, 0)):
        got, _ = lint(text)
        assert got == want, "selftest %s: exit %d, want %d" % (name, got, want)
    print("plan-lint: selftest ok")
    return 0


def main(argv):
    if argv[1:] == ["--selftest"]:
        return selftest()
    if len(argv) != 2:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        code, out = lint(f.read())
    print("\n".join(out))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
