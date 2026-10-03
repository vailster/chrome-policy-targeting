#!/usr/bin/env bash
# Pull the current Chrome policy schemas with GAM7 and regenerate the docs.
set -euo pipefail
cd "$(dirname "$0")/.."

GAM="${GAM:-gam}"
"$GAM" redirect csv ./data/raw_schemas.csv print chromeschemas \
  fields schemaname,validtargetresources,categorytitle,policydescription,policyapilifecycle
python3 scripts/generate.py data/raw_schemas.csv
