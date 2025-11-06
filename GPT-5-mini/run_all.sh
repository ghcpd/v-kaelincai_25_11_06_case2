#!/usr/bin/env bash
set -e
echo "Setting PYTHONPATH"
export PYTHONPATH=$(pwd)
echo "Running Project A tests"
bash Project_A_PreFeature_UI/run_tests.sh
echo "Running Project B tests"
bash Project_B_PostFeature_UI/run_tests.sh
echo "Aggregating results"
python - <<'PY'
import json, pathlib
root = pathlib.Path('.').resolve()
pre = root.joinpath('Project_A_PreFeature_UI','results','results_pre.json')
post = root.joinpath('Project_B_PostFeature_UI','results','results_post.json')
report = root.joinpath('compare_report.md')
pre_r = json.loads(pre.read_text()) if pre.exists() else []
post_r = json.loads(post.read_text()) if post.exists() else []
with report.open('w', encoding='utf-8') as f:
    f.write('# Comparison Report\n\n')
    f.write('Pre results:\n')
    f.write(json.dumps(pre_r, indent=2))
    f.write('\nPost results:\n')
    f.write(json.dumps(post_r, indent=2))
print('Report written to', report)
PY
