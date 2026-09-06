#!/usr/bin/env bash
# Fallback Chinese translation of the core papers with the pdf2zh engine bundled in SuperTranslate's
# venv (Google service, no API key). Used when the DeepSeek balance is exhausted; re-run
# scripts/translate_core.sh <KEY> later to replace these with the higher-quality DeepSeek version.
# Usage: bash scripts/translate_fallback_google.sh [KEY ...]   (defaults to the three core papers)
set -u
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:/usr/local/bin
REPO="$(cd "$(dirname "$0")/.." && pwd)"
P2Z="$HOME/Code/super_translate/.venv/bin/pdf2zh"
TMP="$REPO/translations/p2z_out"
mkdir -p "$TMP" "$REPO/papers/zh" "$REPO/translations/logs"
QUEUE="${*:-EventVLA_2606.20092 TRACE_2606.14551 SAI_2606.16490}"
for name in $QUEUE; do
  src="$REPO/papers/pdf/${name}.pdf"; dst="$REPO/papers/zh/${name}_zh.pdf"
  [ -f "$dst" ] && { echo "[skip] $name (exists)"; continue; }
  echo "=== [$(date +%H:%M:%S)] pdf2zh-google $name ==="
  if "$P2Z" "$src" --service google --lang-out zh --output "$TMP" --thread 4 > "$REPO/translations/logs/${name}.google.log" 2>&1 \
     && cp "$TMP/${name}-mono.pdf" "$dst"; then
    echo "[ok] $name -> $dst ($(pdfinfo "$dst" | rg Pages))"
  else
    echo "[FAIL] $name (see translations/logs/${name}.google.log)"
  fi
done
echo GOOGLE_FALLBACK_DONE
