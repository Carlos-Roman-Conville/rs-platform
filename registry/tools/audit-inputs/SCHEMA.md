# Extraction schema for the registry audit (read-only audit; never edit any source file)

You are helping build a mechanism registry for a simulation platform (see E:/AI Programs/Toolchain/PLATFORM.md §3, §4, §7 if you need context — read it first, it is 12 KB).
A "mechanism" = one causal calculation or rule: a formula, a state-update rule, a lookup table that drives a computation, a threshold rule. Not: pure data lists, UI, file loaders, ids/plumbing (record plumbing only as one row per engine, e.g. "reducer/replay", "scheduler").

Write ONE JSON object per line (JSONL) to your assigned output file. Fields:

{
 "id": "proposed stable id, dotted: <engine>.<area>.<mechanism>, e.g. realism.thermo.conduction, economy.price.rule_base, pirate.body.functional_capacity",
 "name": "short human name",
 "engine": "realism | settlement | economy | pirate-ship (docs) | shared",
 "home": "file path (relative to E:/AI Programs/) and function name or section heading, with line numbers if easy",
 "status": "built (code exists, with tests or used) | documented-only (formula/rule written in a doc, no code) | planned (named as future work)",
 "domain": "A physical | B life | C cognition | D economy | E government | F society | G civilisation | infra",
 "scope": "universal | pirate-specific | mixed (say why in notes)",
 "inputs": [{"name": "...", "unit": "SI or stated unit, or 'unitless'/'unknown'"}],
 "outputs": [{"name": "...", "unit": "..."}],
 "state": "internal state it owns/mutates, or 'stateless'",
 "formulation": "the formula in one line, or a pointer (file §/function) if long",
 "dependencies": ["other mechanisms or data it reads (use ids or names)"],
 "timescale": "tick / update frequency (s, min, hour, day, per event...) or 'unknown'",
 "invariants": "conservation rules / invariants checked, or 'none stated'",
 "sources": "citations or source ids as given; 'none'",
 "evidence": "1-6 per PLATFORM.md §4: 1 physical/math law, 2 empirical statistical, 3 historical observation, 4 simplified sim approximation, 5 hypothetical, 6 fiction. Your best judgement; add '?' if unsure",
 "approximations": "stated limitations/simplifications",
 "tests": "test file + test names/ids that check it, or 'none'",
 "consumers": ["who reads its outputs (functions, engines, docs)"],
 "notes": "anything odd: unit mismatch, same thing computed elsewhere, conflicting values, magic numbers with no source"
}

Be accurate: only record what you actually saw. Prefer fewer, correct rows over guesses. Aim for coverage of every distinct mechanism in your files (typically 15-60 rows for your batch).

Also write a short notes file (markdown, under ~6 KB) listing:
1. Duplicates/overlaps you saw (the same quantity computed or defined in two places — give both homes exactly).
2. Unit problems (mixed units, unitless where a unit is needed, per-day vs per-hour mismatches).
3. Circular dependencies or ownership conflicts.
4. Mechanisms explicitly listed as planned/missing.
5. Pirate-specific things living in a universal engine, or universal things living only in pirate docs.

Files over 40 KB: never read whole — use Grep/search and read sections only. Never edit any file except your two outputs.
Your final reply to me: under 400 words — row count, the most important duplicates/conflicts, anything surprising.
