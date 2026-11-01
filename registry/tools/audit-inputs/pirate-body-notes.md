# Notes: pirate-ship body docs and STATS (engine "pirate-ship (docs)"), 93 rows

Source root: `Games/RPG's/pirate-ship/files/pirate-ship/`. Code compared: `Toolchain/realism/src/*.ts`.

## 0. Key structural finding
- The body docs are **rendered views of data**, not independent specs. `body/build-body-data.py` joins `body/data/*.json` (game adapter columns) with `Toolchain/realism/data/library/*.json` (universal columns, same `id`), renders the tables into the `.md` files between `<!-- table:... -->` markers, and writes `body/data.js` for the dashboard. So the library JSON IS the source of the 16 realism library files; table values in docs cannot disagree with the library. Disagreements are only in **prose formulas** (text outside the markers) versus code.
- realism parses some constants from doc/library prose by regex (e.g. nutrition.ts `/glycogenFactor = .../`, anatomy.ts repair-rate sentence): prose is load-bearing and editing it silently changes code.
- Game-only data files (not in library): `body.json` (record, capabilities, tick, states_of_being, chains, visible_faces), `psychology.json`, `equipment.json` partly, `sources.json` split.
- Docs implemented in realism: anatomy, circulation, medicine, muscular, neurology, nutrition, physiology (+ atmosphere, environment). NOT implemented anywhere: the whole BODY.md capability layer, PSYCHOLOGY, STATS.

## 1. Duplicates / overlaps (doc home vs code home)
- RMR Mifflin: PHYSIOLOGY.md §1 = `realism/src/physics.ts restingMetabolicRate` (also physiology.ts bodyRmr, anatomy.ts speciesRmr). Match.
- Ventilation: PHYSIOLOGY.md §1a = `atmosphere.ts` breathingProcess (not physiology.ts). Match.
- SaO2 Severinghaus: CIRCULATION.md §1a says circulation owns it; code is `atmosphere.ts saturation()`.
- Bleeding rate by class: CIRCULATION.md §2 and MEDICINE.md §3 both describe it; code owner `circulation.ts bleed`.
- Vitamin C to healing/collagen: ANATOMY §2 (tissue integrity) and MEDICINE §7 (healing x3 row) both state the scurvy effect; code has it in both anatomy.ts and medicine.ts healingMultiplier. Risk of two penalties for one cause (the platform's "no second penalty" rule).
- Water need: PHYSIOLOGY §5a and NUTRITION §6 both.
- "State" multiplier: STATS §4 (six items), BODY §2 (three items), PSYCHOLOGY §3 (six items, "not computed here").
- Ageing: STATS §1 age text and PHYSIOLOGY §8 table (same rule).
- Min-max genetic range: STATS attributes and MUSCULAR group min/max (code: muscular.ts) are parallel systems.
- Banister: PHYSIOLOGY §2 (aerobic) vs muscular.ts `muscularBanisterDay` (its own comment says it is not the circulation aerobic_today).
- Constitution drives immunity (MEDICINE §8), healing, seasickness, and BODY constitution_today.

## 2. Unit and value conflicts (doc vs code, doc vs doc)
- **aerobic_today**: PHYSIOLOGY §2/§6 and BODY §3 treat it as an index (divide by 40, ~20-65 mL/kg/min); `circulation.ts` outputs `aerobic_today` = DO2 at maximal cardiac output in **mL O2/min**; PHYSIOLOGY §2 prose says it equals that DO2. Pool formula `Endurance x aerobic_today/40` breaks with the code's number.
- **Banister constants**: prose k1=0.4/42, k2=0.4/7; table k1=1, k2=1.3.
- **Sweat rate**: doc clamp `0.3+0.25 MET+0.1 over` (L/h) vs code ISO 7730 heat-balance derived sweat capped at 2.5 L/h. Doc formula is dead.
- **DO2**: doc has dissolved-O2 term 0.003 PaO2; code is bound O2 only with explicit (1-COHb).
- **Pool formula**: BODY §3 includes heatFactor; PHYSIOLOGY §6 block omits it.
- Pool/fatigue magic constants: `8` MET-h, `0.5 fatigueDay`, `(2-alertness)`, `(1+fatigueDay)`, hunger/fullness rates: no source.
- Attribute scale 1-20 vs "Rex mentioned 30" (open); limb Strength weights invented.

## 3. Circular dependencies / ownership
- PHYSIOLOGY §6 pool reads MEDICINE fever/blood, NUTRITION glycogen; BODY §3 owns the formula; COMBAT spends it. Pool ownership is split BODY/PHYSIOLOGY/COMBAT.
- `drinkFactor` is a STATS state placeholder in BODY §2 while NEUROLOGY (built) already produces the real coordination/arousal outputs: two potential owners.
- Anatomy cascade ↔ circulation regulation loops are intentionally circular (feedback), only partly built.
- PSYCHOLOGY pushes read thresholds owned by three other docs.

## 4. Planned / missing
- Whole BODY.md capability layer (woundDip, coldFactor, hydrationFactor, capFactor, limb Strength, movement, work capacity, accident chance).
- Whole-body Banister aerobic fitness; fatigueDay normalisation; seasickness/sea legs; shivering/heat MET add-ons.
- Electrolyte/glucose/pH pools (anatomy.ts refuses to invent potassium kinetics); clotting from platelets/vitamin K; regulation loops other than kidney volume.
- Hunger/fullness/appetite; starvation stage multipliers; hygiene multiplier table; shock rule; tendon adaptation/injury; strain risk multipliers; effort-required per action; ageing curves consumer; sim levels (aggregate/discovered).
- Cold acclimatisation, altitude: explicitly left out.

## 5. Universal vs pirate classification
**STATS attributes** — universal biology: Strength, Dexterity, Reflexes (per limb), Endurance, Agility, Constitution, Eyesight, Hearing, Taste and smell. Cognition (domain C): Wits, Memory, Perception, Pattern Recognition, Intuition, Spatial Reasoning, Nerve. Pirate gameplay: the 1-20 scale, Poise, Efficiency (spend per action), the eight-function mapping, skills 0-100, rust, talent, claims, all 13 sliders, personality type, hearts/respect/madness/trust. Per-limb split and genetic min-max are universal ideas, the numbers are Rex's design authority.
**BODY.md functional capacity rules** — universal-biology inputs (alertness, woundDip, coldFactor, hydrationFactor, bloodFactor, glycogenFactor, feverFactor), pirate gameplay wrappers (the 1-20 stat scaling, Endurance pool, Efficiency, state multiplier, tiles, accident chance, appearance, states of being). Row ids marked `mixed` or `pirate-specific` accordingly.
**PSYCHOLOGY.md** — all rows domain C (mood, madness, sliders, performance state), pirate-specific.
**Leaks of pirate into universal tables**: MEDICINE healing row "Surgeon skill 50+ dressing daily"; MEDICINE immunity/seasickness driven by Constitution; PHYSIOLOGY ageing table keyed by STATS attribute names; Rex-marked rules ("skills never fall").
**Universal things living only in pirate docs**: sim levels (BODY §8), overnight-tick order (BODY §4), ageing curves (data only), hunger/fullness, seasickness, Banister aerobic fitness.
