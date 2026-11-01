#!/usr/bin/env bash
# Rebuild the registry from curated.py and the audit extracts (*.jsonl). Run from anywhere (Git Bash).
# Writes Toolchain/registry/{mechanisms,graph,quantities,aliases}.json, Toolchain/GRAPH.md and Toolchain/REGISTRY.md.
set -e
cd "$(dirname "$0")"
python build.py > /dev/null
python schema2.py
node --experimental-strip-types uc2.mjs
python vv.py > /dev/null
python render_graph.py > /dev/null
python render_registry.py > /dev/null
echo "registry rebuilt"
