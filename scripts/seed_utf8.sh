#!/usr/bin/env bash
# Seed a UTF-8 file with a placeholder line so that editor tools keep UTF-8 when filling it in.
# Usage: bash scripts/seed_utf8.sh path/to/file.md
set -e; mkdir -p "$(dirname "$1")"; printf "@@BODY@@ 编码种子\n" > "$1"; echo "seeded $1"
