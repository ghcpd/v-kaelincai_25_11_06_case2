#!/usr/bin/env bash
set -e
# Run Project A tests
bash Project_A_PreFeature_UI/run_tests.sh
# Run Project B tests
bash Project_B_PostFeature_UI/run_tests.sh

# Copy results
mkdir -p shared_artifacts/results
cp Project_A_PreFeature_UI/results/* shared_artifacts/results/ || true
cp Project_B_PostFeature_UI/results/* shared_artifacts/results/ || true
cp Project_A_PreFeature_UI/results/*.png shared_artifacts/ || true
cp Project_B_PostFeature_UI/results/*.png shared_artifacts/ || true

# Generate simple compare report
python - <<'PY'
import json, glob, os
pre = json.load(open('Project_A_PreFeature_UI/results/results_pre.json'))
post = json.load(open('Project_B_PostFeature_UI/results/results_post.json'))
report = {
 'pre': pre,
 'post': post
}
with open('shared_artifacts/compare_report.md', 'w') as f:
    f.write('# Compare Report\n\n')
    f.write('## Summary\n')
    f.write('| test_id | pre_overlaps | post_overlaps |\n')
    f.write('|---|---:|---:|\n')
    for p, q in zip(pre, post):
        f.write('| {} | {} | {} |\n'.format(p['id'], p.get('overlaps', 'error'), q.get('overlaps', 'error')))
    f.write('\n\n')
    f.write('### Charts\n')
    imgs = glob.glob('Project_A_PreFeature_UI/results/*.png') + glob.glob('Project_B_PostFeature_UI/results/*.png')
    for img in imgs:
        f.write('![](%s)\n\n' % img)
PY

echo "Completed run_all.sh: See shared_artifacts/compare_report.md"
