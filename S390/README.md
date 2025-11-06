# Evaluation of Chart Label Enhancement

This repository contains two projects demonstrating pre- and post-enhancement versions of a charting platform focusing on label overlap and readability.

- Project_A_PreFeature_UI: Basic implementation with static label placement that may overlap.
- Project_B_PostFeature_UI: Improved implementation that dynamically adjusts label placement and enhances contrast.

How to run:
- For Linux/macOS: run `./run_all.sh`
- For Windows (PowerShell): run `./run_all.ps1`

Each project contains its own `run_tests.sh` (and PowerShell `run_tests.ps1`), `requirements.txt`, and tests. Test data is located at `test_data.json`.

See `compare_report.md` for the final comparison and `shared/screenshots` for before/after images.\n\nProject B improvements include:\n- Dynamic label placement to avoid overlaps (iterative repositioning with collision checks)\n- Optimized font size and label color contrast using WCAG-inspired contrast checks\n- Additional test metrics (min vertical gap, overlap detection, contrast checks)
