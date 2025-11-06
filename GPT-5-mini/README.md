# Evaluation of Enhancement: Chart Label Improvements

This workspace contains two projects:
- Project_A_PreFeature_UI — baseline with overlapping labels.
- Project_B_PostFeature_UI — improved label placement avoiding overlap.

Run the tests with:

1. Create a virtual environment and install dependencies for both projects:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r Project_A_PreFeature_UI/requirements.txt; pip install -r Project_B_PostFeature_UI/requirements.txt
```

2. Run all tests and produce comparison:

```powershell
bash run_all.sh
```

Artifacts (results, logs, screenshots) are placed under each project's `results` and `logs` directories.
