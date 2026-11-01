# Toolchain

## What this is

The shared tools that build everything else. Under principle 3 this scope is what makes every other scope faster.

## What's under it

| Folder | What | State |
|---|---|---|
| [ask-cursor/](ask-cursor/) | Sends gated work to Composer (Cursor). | active |
| [ask-codex/](ask-codex/) | Sends engine work to Codex (ChatGPT Pro). | active |
| [card-fetch/](card-fetch/) | Polite fetcher for card data and rules pages. | active |
| [ludii/](ludii/) | Local Ludii, the source for traditional-game rules (read, never copied). | active |
| [realism/](realism/) | The Reality & Species engine (physics, chemistry, environment, biology); the pirate ship its first client. | active |
| [settlement/](settlement/) | The settlement engine (land, property, buildings, businesses, workforce); built to step 2, the pirate town its first client. | active |

Owners, boundaries and the planned Economy, Government and Cognition engines: [ENGINES.md](ENGINES.md).

The games belt (`Games\Card Games\_agent\`) is toolchain too but lives with the games repo, since it runs there.

## Read first

- The `README.md` of the tool you're using or changing.

## Skim

- None.

## Ignore

- `ludii/` jars and game files beyond the one you need.

## Rules that apply here

Inherited from [HQ/PRINCIPLES.md](../HQ/PRINCIPLES.md), plus:

- Other scopes call these tools by path. Moving or renaming one breaks its callers; update them in the same change.

## Current state

- 2026-10-23: moved here from `utilities\`. Callers (the games belt, `.claude\launch.json`, scripts) still point at `utilities\` and need updating.
