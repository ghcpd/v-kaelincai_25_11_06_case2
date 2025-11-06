# Evaluation of Model Improvements on Chart Labeling

This workspace contains two projects:
- `Project_A_PreFeature_UI`: baseline chart generator with static labels (may overlap).
- `Project_B_PostFeature_UI`: improved chart generator with dynamic label placement and contrast improvements.

Quick start (Bash):
1. Install dependencies: `bash Project_A_PreFeature_UI/setup.sh` and `bash Project_B_PostFeature_UI/setup.sh`
2. Run both tests: `bash run_all.sh`

On Windows PowerShell:
1. `bash Project_A_PreFeature_UI/setup.sh; bash Project_B_PostFeature_UI/setup.sh`
2. `./run_all.ps1`

Acceptance criteria:
- In Project A, the tests should detect label overlaps for at least one test case.
- In Project B, the tests should detect no label overlaps for the non-malformed test cases.

See `shared_artifacts/compare_report.md` for a summary and visual evidence.
