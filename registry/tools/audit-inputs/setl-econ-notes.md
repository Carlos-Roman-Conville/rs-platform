# Settlement + Economy audit notes (58 rows in setl-econ.jsonl)

CONTRACTS.md: settlement/ and economy/ copies are byte-identical (md5 b1ab37dd...). Unread by me: MIGRATION.md, DEPENDENCIES.md tail, TESTS.md tail, pirate-repo adapter (I1/I2 live there).

## 1. Duplicates / overlaps
- Stock creation, 3 paths: settlement `tick/production.ts` Q -> `produce`; economy `tick/index.ts production()` abstract markets (`productionPerDay`); host `addStock`. Separated only by `Market.mode`.
- Production record twice: settlement `DayProduction` (per line, latest day) vs economy `MarketGood.producedLast` (per good). Contract says economy reads `reader.production`; code never does, it counts via its own `produce`.
- Loss-over-time, 3 notions: settlement `tick/decay.ts` (building condition), economy `spoilage()` (goods, fraction/day), realism decay. All constant daily rates, unrelated rules.
- Wages vs labour market: settlement `tick/wages.ts` pays a fixed `Post.wage`; economy `labour.ts wageQuote` is a pure query nothing consumes (needs host `setWage`, blocked by Q10 / s12.6).
- Two labour-supply interfaces: settlement `LabourProvider.draw/available/productivity` and economy `LabourSupplyProvider.supply`. Neither has an implementation.
- Ledger: settlement owns `accounts`/`ledger`; economy `StubLedger` + `LedgerRow` structurally duplicate `Transaction`.
- Equipment list: `ProductionLine.equipment` (settlement) copies `Recipe.equipment` (economy); `Rates` interface declared in both.
- `reduce/Runner/ctx/mint/must/finite` helpers copied in both engines (also true for realism, per the pattern).
- Shortage computed twice in economy: unclamped in `consumption()`, clamped in `queries.shortage()`.
- Sale price: settlement `sell` takes explicit price; economy `PriceProvider.valueOf` declared but never called or implemented.
- Burial/sanitation/land use scoped in both: settlement PACKAGES s8 (Q16-18) and economy PLAN step 12.

## 2. Unit problems
- Time unit is the **day** everywhere (rent/day, wage/day, decayPerDay, spoilagePerDay, per-day five numbers, shipment days). Only hour use: `Post.hours` / `config.hoursPerDay` (=10) scaling labour-days. Wage is per day and does not scale with hours; economy median ignores hours.
- Two independent day counters: `settlement.day` (incremented at end of its tick) and `economy.day`. Contract s9 says `economy.tick(N)` but the command has no day argument; `StubLedger.day` is set by hand. Host must sync three clocks.
- Money, weight, volume have no unit: `Good.weight` stored, never used; currency unitless; stock real-valued with 1e-9 epsilon.
- `Shipment.arrives = day + days` assumes integer days; not enforced.
- Condition is 0..1 unitless; band decay/outputFactor placeholders.

## 3. Circular / ownership conflicts
- **Inventory ownership**: `Project.account` is used as money holder (pay) AND inventory id (`materials.have/take` in `tick/projects.ts`). Economy keys inventories by `inv.*` with a separate `holder`. Adapter must make them coincide or this breaks.
- Business money identity: `Business.account` = `acct.*`, ledger holder = `biz.*`.
- Contract s9 vs economy tick: promised "market clearing, labour quotes, accounting snapshots" in `economy.tick`; code has none (quotes and accounts are queries, no clearing).
- Contract s8 vs `accounts()`: no cost-of-goods or spoilage line.
- Contract s6: equipment presence via `reader.hasFixture`; economy src never calls it (3 of 4 reader methods unused).
- Mutual dependency by order: settlement.tick calls economy `produce` (needs economy inventories writable) and economy then reads settlement output. Works via day order, not circular in code.
- `credit`/`debit` commands create/destroy money outside conservation; no money-supply owner.

## 4. Planned / missing
- Realism hooks: population/nutrition provider (PLAN step 11, test I3), UtilityProvider (stub = Infinity), TransportProvider real map.
- King-Davenant price curve (RESEARCH s1, unbuilt, needs Rex), burial/waste flows E15/E16, cemeteries/sanitation/land use.
- Not present at all though mission asks: structure/material needs per building (lumber per wall, techniques), tool/knowledge/tech gating in recipes, household budgets and income-driven demand, price discovery/market clearing, taxes/duties (future Government engine), labour skill/learning, money supply, mass/energy balance in production.

## 5. Pirate-specific in universal engines
- src/ is clean of pirate words. Leaks are conventions: `isPool` uses `'pool.'` prefix; `'labourer'` role and `'pool.default'` hard-coded in project step; settlement `state.ts` comment mentions the 25 facility ids; example uses `port.north/east/south` (placeholder, in examples only).
- `ship.*` id prefix means shipment, not vessel (confusable with pirate ship entity).
- Pirate-specific research sits in docs: economy RESEARCH.md (1690-1720 Caribbean wages, King-Davenant 17th c. England), settlement QUESTIONS (Q1,Q5,Q6,Q7,Q10,Q11 about the 16 `port.*` places), `port.cash` treasury (Q7).
- Universal things living only in pirate docs: GOODS.md recipes/quantities/goods types, ports.json produces/consumes, occupations, POPULATION.md pools.

## Open questions and what each blocks
Settlement QUESTIONS.md (Q2, Q1/Q6 partly answered):
- Q1 footprint classes/household size/reserve share: map derivation (MIGRATION step 3, T2).
- Q3 meaning of "developed": step 10, T14 (story).
- Q4 operator rebinding alignment shaper: step 6 (story).
- Q5 starting fixtures per place: step 5, T6; also "idle fixture counts" (activeOnly) = CONTRACTS s12.7 / reader.hasFixture default.
- Q6 starting title holders/purchasability: steps 4,6; T3,T5,A1.
- Q7 is `port.cash` the treasury: step 4; CONTRACTS s12.2 (ledger holder).
- Q8 free layout: step 8, U8/T11 (default off).
- Q9 inheritance custom: step 4, T4 (note: README/CONTRACTS cite Q9 as idle-fixture; QUESTIONS.md Q5 has that and Q9 is inheritance, an id inconsistency).
- Q10 post counts, lines, wage and rent levels: steps 6,7, T9; CONTRACTS s12.6 (may a quote move wages), blocks wiring wage_quote to setWage.
- Q11 how mayor's office is won/powers: step 9, T13.
- Q12 events story hears: step 10.
- Q13 placement; Q14 second consumer: step 1/11.
- Q15 labour sharing across lines: step 7, T9 (production labour_cap order rule).
- Q16 cemeteries, Q17 sanitation, Q18 land use: unscheduled; Q18 blocks step 3 land-use.
CONTRACTS s12 (collected):
1. Goods types/money vs goods/grain/cask (GOODS.md Open 1-8): blocks `Good.type` semantics, money-as-good.
2. `port.cash` treasury (= Q7).
3. Who values property for unpriced sale: blocks calling `PriceProvider.valueOf`.
4. Are named characters' spending simulated or only pools': blocks household consumption/income mechanism.
5. Price formula and constants: blocks economy.price.rule beyond `base` (and king_davenant).
6. Wage levels per trade and whether a quote may move wages (= Q10): blocks wage quote effect.
7. Idle fixture counts for "has it" (Settlement Q9 in contract numbering = Q5 in QUESTIONS file).
