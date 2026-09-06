#!/usr/bin/env bash
# Translate every paper in a lane file (key<TAB>arxiv_id per line) with scripts/translate_core.sh.
# Skips papers whose Chinese PDF exists with a zero-error inspect report, and papers whose English PDF
# is not downloaded yet. Several lanes may run concurrently on disjoint lane files.
# Usage: bash scripts/translate_queue.sh scripts/lane_a.txt
set -u
LANE="$1"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
ok=0; fail=0; skip=0
while IFS=$'\t' read -r key aid; do
  [ -z "${key:-}" ] && continue
  case "$key" in \#*) continue;; esac
  name="${key}_${aid}"
  pdf="$REPO/papers/pdf/$name.pdf"; zh="$REPO/papers/zh/${name}_zh.pdf"; rep="$REPO/papers/zh/${name}_zh.inspect.json"
  if [ ! -f "$pdf" ]; then echo "[skip] $name (no English PDF yet)"; skip=$((skip+1)); continue; fi
  if [ -f "$zh" ] && [ -f "$rep" ] && python3 -c "import json,sys; d=json.load(open('$rep')); sys.exit(0 if not [i for i in d.get('issues',[]) if i.get('severity')=='error'] else 1)" 2>/dev/null; then
    echo "[skip] $name (done, inspect clean)"; skip=$((skip+1)); continue
  fi
  echo "=== [$(date +%H:%M:%S)] $name"
  if bash "$REPO/scripts/translate_core.sh" "$name" --skip-overflow > /dev/null 2>&1; then ok=$((ok+1)); echo "[ok]   $name"
  else fail=$((fail+1)); echo "[FAIL/QA] $name (see translations/logs/$name.log and papers/zh/${name}_zh.inspect.json)"; fi
done < "$LANE"
echo "LANE DONE ok=$ok fail=$fail skip=$skip"
