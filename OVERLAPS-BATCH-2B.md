# Overlap groups, batch 2b (registry keeper, 2026-10-31)

**Status: approved by Rex 2026-10-31 evening (all five owners as proposed; DUP-61 collective knowledge under Knowledge & Technology).** Was: proposed, for Rex (presented by the controller together with X1, the first integrated experiment). Batch
2b covers the seams between the engines that are being staffed tonight, where a second gear is most likely to be built
by mistake: organisations, households, transmission, collective knowledge and office powers. Same form as batches 1
and 2. For each group Rex is asked one thing: **approve the proposed owner, change it, or hold it.** Approval starts
nothing by itself: each group starts only when the keepers named under "must agree" accept the ownership and the
acceptance test. Nothing is deleted; a losing home becomes a read, an aggregate, a view or a restatement.

Unlike batches 1 and 2, four of the five groups are **ownership gaps between planned rows**: nothing is built on the
new side yet. Approving them now means each new keeper designs against one owner from the first line, instead of the
registry closing a duplicate later. Two groups each touch one built row (DUP-58 Economy and Settlement, DUP-62
Settlement).

A group closes under the same criteria as batches 1 and 2 (PLATFORM.md §11a): **implemented** (the acceptance test
passes); **integrated** (a combined test of the owner with every former home that now reads it); **validated**
(against independent evidence within a declared tolerance where it exists, or a recorded "no independent data" with
the experiment that would test it). Social mechanisms will mostly carry evidence levels 3–5 (PLATFORM §4); the
acceptance tests below are about **single authority**, not about the social science being right.

## Summary

| # | Group | Authority | Proposed owner of the state | Built today | Must agree | Also needs Rex | Run as |
|---|---|---|---|---|---|---|---|
| 1 | DUP-58 organisations | ownership gap | **Society** (`society.organisation.actors`): the organisation as an actor (membership, leadership, decisions); Economy keeps its accounts and holdings, Settlement its legal records | `economy.org.organisation` (Economy), `settlement.business.open` (Settlement) | Society, Economy, Settlement | — | design (Society keeper); Economy adapter unit later |
| 2 | DUP-59 households | ownership gap | **Society** (`society.household.structure`): who belongs, kinship, marriage, inheritance custom; Economy's budget is a view keyed by the Society household id | nothing | Society, Economy | — | design |
| 3 | DUP-60 transmission | shared part | **Society's network** (`society.network.communication`) as the one transmission substrate; preferences, norms, doctrines and techniques are content carried on it; Reality's transmission stays the physical channel | nothing | Society, Cognition, Knowledge & Technology, Reality | — | design |
| 4 | DUP-61 collective knowledge | ownership gap | **Knowledge & Technology** (`knowledge.collective.stock`) as an aggregate over minds and surviving records, with loss; Society's network the substrate; Cognition each mind's belief | `cognition.belief.update` (the per-mind side) | Knowledge & Technology, Society, Cognition, History | whether "what the town knows" is K&T's or Society's | design |
| 5 | DUP-62 office powers | ownership gap | **Government** for what an office may do and how authority passes; **Settlement** keeps who holds which office and the permits issued, written through commands | `settlement.authority.office_powers` (Settlement) | Government, Settlement | — | design (Government keeper); a Settlement doc unit later |

Order: all five are design-time decisions and can be approved together; none waits on another group. DUP-60 should
be agreed before DUP-61 (the stock rides on the network).

## 1. DUP-58 — organisations

- **Today:** `economy.org.organisation` (built, domain F) keeps organisations as economic holders; Settlement's
  businesses (`settlement.business.open`, built) are organisations with premises and posts; ROADMAP P6 plans
  "organisations as actors" in Society (`society.organisation.actors`, planned), and Rex's institutions rule makes
  institutions out of organisations (`society.institution.formation_dissolution`, planned).
- **Authority:** ownership gap: three engines would each hold "the organisation".
- **Proposed owner:** Society owns the organisation as an actor (its id, members, leadership, rules, obligations,
  decisions taken through its members' minds). Economy's organisation becomes the **economic view** of the Society
  actor (accounts, holdings, keyed by the Society id); a Settlement business is the **legal and premises view**
  (titles, posts, ledger).
- **Becomes a view:** `economy.org.organisation` reads the Society id; Settlement keeps its business record and
  points at the actor that owns it.
- **Acceptance test:** (1) one organisation id across the three engines; (2) creating, merging or dissolving an
  organisation happens only in Society and propagates to the two views; (3) no Economy or Settlement mechanism decides
  membership or leadership.
- **Must agree:** Society, Economy, Settlement.
- **Note:** until Society is built, Economy and Settlement keep working as today; the view keys arrive with Society's
  first unit.

## 2. DUP-59 — households

- **Today:** two planned homes: P5 Economy households (income, budget, consumption; CONTRACTS §12.4,
  `economy.household.budget`) and P6 Society households (marriage, kinship, inheritance customs,
  `society.household.structure`). Nothing built.
- **Authority:** ownership gap.
- **Proposed owner:** Society owns the household (who belongs, kinship, marriage, inheritance custom); Economy owns
  the household **budget** as a view keyed by the Society household id (income, spending, consumption).
- **Acceptance test:** one household id; membership changes (birth, death, marriage, departure) happen only in
  Society; a household's budget follows its membership without a second membership list in Economy.
- **Must agree:** Society, Economy.

## 3. DUP-60 — transmission

- **Today:** four planned homes: Society's preference transmission (`society.transmission.preferences`, IF-12),
  Society's communication networks (`society.network.communication`, IF-16), Knowledge & Technology's diffusion of
  techniques (`knowledge.technology.diffusion`, P9), and Reality's physical transmission of a message
  (`realism.communication.transmission`). Doctrine transmission (`society.doctrine.transmission_divergence`) has since
  been registered on the network (IF-45).
- **Authority:** shared part: distinct contents that must share one carrier.
- **Proposed owner:** Society's network is **the one transmission substrate** (who is linked to whom, how often, how
  trusted); preferences, norms, doctrines and techniques are **content** carried on it; Reality's transmission stays
  the physical channel (distance, sound, light, a carried letter); Cognition owns what each mind encodes, understands
  and believes.
- **Becomes content:** preference, doctrine and technique transmission become content types on the network, never
  networks of their own.
- **Acceptance test:** (1) one network; (2) a rumour, a doctrine and a technique spreading through the same village
  travel the same links with their own content rules; (3) cutting a link (death, quarrel, suppression) stops all three.
- **Must agree:** Society, Cognition, Knowledge & Technology, Reality.

## 4. DUP-61 — collective knowledge

- **Today:** Rex's history rule (2026-10-31) flagged "collective knowledge stocks with loss, the bridge between one
  mind's belief and what the town knows" as unowned; registered as planned `knowledge.collective.stock`
  (`society.knowledge_stock`); the per-mind side is the built `cognition.belief.update`; diffusion and the network sit
  in DUP-60.
- **Authority:** ownership gap at the seam of Cognition, Society and Knowledge & Technology.
- **Proposed owner:** Knowledge & Technology owns the collective stock as an **aggregate** over members' beliefs and
  surviving records, with loss when holders die, records decay or transmission fails; Society's network is its
  substrate; Cognition owns each belief. Nobody else builds "what the town knows".
- **Acceptance test:** (1) the stock is computed from minds and records, never stored as a separate truth; (2) when
  the last holder of a technique dies and no record survives, the stock loses it; (3) History reads the stock only for
  validation, never feeds it.
- **Must agree:** Knowledge & Technology, Society, Cognition, History.
- **Also needs Rex:** whether the collective stock is Knowledge & Technology's (the registry's proposal: K&T is
  "recorded and transmitted knowledge with loss", Rex) or Society's (it is a property of a community).

## 5. DUP-62 — office powers

- **Today:** `settlement.authority.office_powers` (built) records offices, permits and permissions; ROADMAP P8 gives
  "offices' powers" to Government with "Settlement keeps the records"; Rex's institutions rule registers Government's
  authority acquisition and delegation and institutional succession (planned).
- **Authority:** ownership gap: Settlement's built row holds both who holds an office and, in part, what it permits.
- **Proposed owner:** Government owns **what an office may do** and **how authority passes** (delegation,
  succession); Settlement keeps **the record** of who holds which office and the permits issued, written through
  commands that Government's decisions issue.
- **Becomes a record:** Settlement's office row stays the register; the decision of what an office may grant moves to
  Government when it is built.
- **Acceptance test:** (1) a permit is issued only when Government's rules allow that office to grant it; (2) a
  succession changes the office holder only through a Settlement command issued by Government; (3) no Settlement
  mechanism decides what an office may do.
- **Must agree:** Government, Settlement.
- **Note:** Settlement's current behaviour stays until Government exists; the change is one Settlement doc unit now
  (marking the powers part as Government's) and a code unit when Government's first rows are built.

## Tracking

| # | Group | State | Approved owner | Keepers to agree | Agreed | Units queued | Closed (commit) | Re-audit |
|---|---|---|---|---|---|---|---|---|
| 1 | DUP-58 organisations | closing: **agreed (amended)** | Society (actor); Economy and Settlement views | Society, Economy, Settlement | 2026-10-31 Society, Economy, Settlement: one Society actor id per business (an actor may run several); actor lifecycle only in Society; no name/kind/member/leader in economy state; unknown Society ids refused; money only on Settlement's ledger, one kernel transaction; merger/dissolution transfers open for Rex; Settlement 2026-10-31 agrees (4): ledger rows via LedgerProvider in one transaction, Settlement decides no amounts, Q19 unpaid dues open | — | — | — |
| 2 | DUP-59 households | closing: **agreed (amended)** | Society (household); Economy budget view | Society, Economy | 2026-10-31 Society, Economy: membership via a Society provider; no member list in economy state; one household per person; ECON-8 open | — | — | — |
| 3 | DUP-60 transmission | closing: **agreed (amended)** | Society's network, one substrate | Society, Cognition, K&T, Reality | 2026-10-31 Society, K&T, Cognition: one network, contact opportunities only; trust stays Cognition's; per-channel content rules (K&T); one entry point into a mind; Reality 2026-10-31: physical arrival only, phase 8; link cuts from Life's death ledger | — | — | — |
| 4 | DUP-61 collective knowledge | closing: **agreed (amended)** | Knowledge & Technology (Rex) | K&T, Society, Cognition, History | 2026-10-31 K&T, Society, Cognition: known vs invented on a surviving record; unread records not known; summary-run mean test; no mind reads the stock; History 2026-10-31: read-only record phase, identical hashes attached or detached, K-4 write rule, G-once | — | — | — |
| 5 | DUP-62 office powers | closing: **agreed (amended)** | Government (powers, succession); Settlement (records) | Government, Settlement | 2026-10-31 Government, Settlement: every power check via AuthorityProvider.may; succession via appoint/vacate/inherit; default provider is host setup data; byte-identical thirty-day outputs without Government | settlement 2781 (doc) | — | — |

## Rex's decisions

(empty until Rex decides; the registry keeper records them as `DECISIONS` entries in `registry/tools/curated.py`)
