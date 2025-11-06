#!/usr/bin/env bash
set -e
echo "Running Project A tests..."
(cd Project_A_PreFeature_UI && bash setup.sh && bash run_tests.sh)
echo "Running Project B tests..."
(cd Project_B_PostFeature_UI && bash setup.sh && bash run_tests.sh)
# Copy results to shared
mkdir -p shared_artifacts
cp Project_A_PreFeature_UI/results/results_pre.json shared_artifacts/results_pre.json || true
cp Project_B_PostFeature_UI/results/results_post.json shared_artifacts/results_post.json || true
python - <<'PY'
import json
import os
p='shared_artifacts'
pre=json.load(open(os.path.join(p,'results_pre.json')))
post=json.load(open(os.path.join(p,'results_post.json')))
report={'pre':pre,'post':post}
open(os.path.join(p,'compare_report.json'),'w').write(json.dumps(report,indent=2))
print('Wrote compare_report.json')
PY
