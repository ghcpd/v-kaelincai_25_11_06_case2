# Quick Reference Guide

## One-Command Execution

### Windows (PowerShell)
```powershell
.\run_all.ps1
```

### Linux/Mac (Bash)
```bash
chmod +x run_all.sh
./run_all.sh
```

## Project Structure

```
chatWorkspace/
├── Project_A_PreFeature_UI/      # Pre-Enhancement (broken)
├── Project_B_PostFeature_UI/      # Post-Enhancement (fixed)
├── test_data.json                 # Test cases
├── compare_report.md              # Generated comparison
├── run_all.ps1 / run_all.sh      # Master test runner
└── README.md                      # Full documentation
```

## Key Files

| File | Purpose |
|------|---------|
| `test_data.json` | 6 test cases (JSON format) |
| `run_all.ps1/.sh` | Run everything |
| `compare_report.md` | Results comparison (generated) |
| `README.md` | Complete documentation |
| `PROJECT_SUMMARY.md` | Technical summary |

## Expected Results

### Project A (Pre-Enhancement)
- **Pass Rate**: ~16.7% (1/6 tests)
- **Issues**: Label overlaps, poor accessibility
- **Charts**: `Project_A_PreFeature_UI/results/charts/`

### Project B (Post-Enhancement)
- **Pass Rate**: 100% (6/6 tests)
- **Improvements**: No overlaps, WCAG AAA compliant
- **Charts**: `Project_B_PostFeature_UI/results/charts/`

## Test Cases

| ID | Type | Description |
|----|------|-------------|
| TC001 | Normal | Basic bar chart (5 points) |
| TC002 | Edge | High-density chart (15 points) |
| TC003 | Boundary | Similar values causing overlap |
| TC004 | Complex | Multi-series chart (3 series) |
| TC005 | Malformed | Missing/null labels |
| TC006 | Extreme | Very large values (millions) |

## Key Metrics

| Metric | Pre | Post | Improvement |
|--------|-----|------|-------------|
| Contrast Ratio | 2.5:1 | 7.2:1 | +188% |
| Test Pass Rate | 16.7% | 100% | +83.3 pts |
| Label Overlaps | Yes | No | ✅ Fixed |
| WCAG AA | ❌ Fail | ✅ Pass | ✅ Fixed |
| WCAG AAA | ❌ Fail | ✅ Pass | ✅ Fixed |

## Common Commands

### Run Individual Projects
```powershell
# Project A
cd Project_A_PreFeature_UI
.\setup.ps1
.\run_tests.ps1

# Project B
cd Project_B_PostFeature_UI
.\setup.ps1
.\run_tests.ps1
```

### Generate Report Only
```powershell
python generate_comparison_report.py
```

### Verify Structure
```powershell
.\verify_structure.ps1
```

### View Results
```powershell
# JSON results
type Project_A_PreFeature_UI\results\results_pre.json
type Project_B_PostFeature_UI\results\results_post.json

# Comparison report
type compare_report.md

# Logs
type Project_A_PreFeature_UI\logs\log_pre.txt
type Project_B_PostFeature_UI\logs\log_post.txt
```

## Troubleshooting

### Python not found
```powershell
# Install Python 3.8+
# https://www.python.org/downloads/
```

### Permission denied
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Module not found
```powershell
# Activate virtual environment first
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Tests fail unexpectedly
```powershell
# Check logs
type logs\log_pre.txt
type logs\log_post.txt

# Verify Python version
python --version  # Should be 3.8+
```

## Output Locations

### Charts
- Pre: `Project_A_PreFeature_UI/results/charts/*.png`
- Post: `Project_B_PostFeature_UI/results/charts/*_enhanced.png`

### Results
- Pre: `Project_A_PreFeature_UI/results/results_pre.json`
- Post: `Project_B_PostFeature_UI/results/results_post.json`

### Logs
- Pre: `Project_A_PreFeature_UI/logs/log_pre.txt`
- Post: `Project_B_PostFeature_UI/logs/log_post.txt`

### Report
- Comparison: `compare_report.md`

## Timeline

1. **Setup** (~1 min): Create virtual environments, install dependencies
2. **Project A Tests** (~30 sec): Run pre-enhancement tests
3. **Project B Tests** (~40 sec): Run post-enhancement tests
4. **Report Generation** (~5 sec): Create comparison report
5. **Total** (~2-3 minutes)

## Success Criteria

✅ All files generated  
✅ Project A: 1/6 tests pass (expected failures)  
✅ Project B: 6/6 tests pass  
✅ Charts show visual improvements  
✅ Comparison report generated  
✅ Accessibility metrics improve  
✅ No label overlaps in Project B  

## Next Steps

1. Run verification: `.\verify_structure.ps1`
2. Run full suite: `.\run_all.ps1`
3. Review comparison: Open `compare_report.md`
4. View charts: Open files in `results/charts/`
5. Check metrics: Open `results_*.json` files

## Support

- Full docs: `README.md`
- Technical summary: `PROJECT_SUMMARY.md`
- Test data: `test_data.json`
- Interactive guide: `.\quick_start.ps1`

---

**Status**: Ready for Evaluation  
**Version**: 1.0  
**Updated**: 2025-11-06
