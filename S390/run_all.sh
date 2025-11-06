#!/usr/bin/env bash
set -e
ROOT=$(pwd)
# Run Project A tests
pushd Project_A_PreFeature_UI
chmod +x ./run_tests.sh || true
./run_tests.sh || true
popd

# Run Project B tests
pushd Project_B_PostFeature_UI
chmod +x ./run_tests.sh || true
./run_tests.sh || true
popd

# Aggregate results
mkdir -p shared/reports
cp Project_A_PreFeature_UI/results/results_pre.json shared/reports/ || true
cp Project_B_PostFeature_UI/results/results_post.json shared/reports/ || true
cp Project_A_PreFeature_UI/results/*.png shared/screenshots || true
cp Project_B_PostFeature_UI/results/*.png shared/screenshots || true

# Generate a simple compare_report.md
python - <<PY
import json,os
rA='Project_A_PreFeature_UI/results/results_pre.json'
rB='Project_B_PostFeature_UI/results/results_post.json'
resA = json.load(open(rA)) if os.path.exists(rA) else []
resB = json.load(open(rB)) if os.path.exists(rB) else []
with open('compare_report.md','w') as f:
    f.write('# Comparison Report\n\n')
    f.write('## Results Summary\n')
    f.write('- Project A tests: %d\n' % len(resA))
    f.write('- Project B tests: %d\n' % len(resB))
    f.write('\n')
    f.write('## Summary Table\n')
    f.write('| Test ID | Pre Overlap | Post Overlap | Pre Min Gap (px) | Post Min Gap (px) | Post Low Contrast |\n')
    f.write('|---------|-------------|--------------|------------------:|-------------------:|-------------------:|\n')
    ids = sorted(set([r['id'] for r in (resA+resB)]))
    for id in ids:
        pa = next((r for r in resA if r['id']==id), {})
        pb = next((r for r in resB if r['id']==id), {})
        f.write('| %s | %s | %s | %s | %s | %s |\n' % (
            id,
            pa.get('detected_overlap', 'N/A'),
            pb.get('detected_overlap', 'N/A'),
            pa.get('min_vertical_gap_px', 'N/A'),
            pb.get('min_vertical_gap_px', 'N/A'),
            pb.get('low_contrast', 'N/A')
        ))
    f.write('\n')
PY

echo "All done. See compare_report.md and shared/screenshots for artifacts."