#!/usr/bin/env bash
# verify-deploy.sh — post-deploy HTTP 200 check for kalistorik.com
# Usage: ./scripts/verify-deploy.sh (needs git, curl, proxy at 127.0.0.1:7890)
set -euo pipefail
PROXY="socks5h://127.0.0.1:7890"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
fail=0
echo "=== verify-deploy ==="
for f in $(cd "$REPO" && git ls-files '*.html' '*.xml'); do
  code=$(curl --proxy "$PROXY" -s -o /dev/null -L -w "%{http_code}" "https://kalistorik.com/$f")
  if [ "$code" != "200" ]; then echo "  [$code] $f ❌"; fail=1; else echo "  [200] $f"; fi
done
if [ "$fail" -eq 0 ]; then echo "✅ verify-deploy passed"; else echo "❌ verify-deploy failed"; exit 1; fi
