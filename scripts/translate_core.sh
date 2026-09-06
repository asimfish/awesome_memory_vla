#!/usr/bin/env bash
# Translate one core paper PDF into Chinese with SuperTranslate (layout-preserving, DeepSeek backend)
# and run its object-level QA inspection. Output lands in papers/zh/<key>_zh.pdf next to the
# translation cache and inspect report. Usage: bash scripts/translate_core.sh EventVLA_2606.20092
set -uo pipefail
KEY="$1"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
ST=/Users/liyufeng/Code/super_translate
export SUPER_TRANSLATE_HOME="$ST"
# API key is read from the local PDFMathTranslate config and exported only as an env var (never echoed).
export DEEPSEEK_API_KEY="$(python3 -c "import json; d=json.load(open('/Users/liyufeng/.config/PDFMathTranslate/config.json')); print([t['envs']['DEEPSEEK_API_KEY'] for t in d['translators'] if t['name']=='deepseek'][0])")"
IN="$REPO/papers/pdf/$KEY.pdf"
OUT="$REPO/papers/zh/${KEY}_zh.pdf"
LOG="$REPO/translations/logs/$KEY.log"
mkdir -p "$REPO/papers/zh" "$REPO/translations/logs"
echo "=== $(date '+%F %T') START $KEY" | tee -a "$LOG"
if bash "$ST/skills/paper-translate/scripts/translate_one.sh" "$IN" "$OUT" "${@:2}" >> "$LOG" 2>&1; then
  echo "=== $(date '+%F %T') OK   $KEY -> $OUT" | tee -a "$LOG"
else
  echo "=== $(date '+%F %T') FAIL $KEY (see $LOG)" | tee -a "$LOG"; exit 1
fi
