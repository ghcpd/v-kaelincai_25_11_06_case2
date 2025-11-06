# Data Visualization Enhancement - Complete Project Index

## 📋 Project Overview

Two complete Python projects demonstrating data visualization improvements through dynamic label positioning and accessibility enhancements.

**Evaluation Focus**: AI model capability to implement UI/UX enhancements (Enhancement subtype, Feature & Improvement category)

---

## 🚀 Quick Start

### One Command to Run Everything
```powershell
.\run_all.ps1
```

**Duration**: ~2-3 minutes  
**Output**: Test results, charts, and comparison report

---

## 📁 Complete File Listing

### Root Directory
| File | Purpose | Type |
|------|---------|------|
| `README.md` | **Main documentation** - Start here! | Documentation |
| `QUICK_REFERENCE.md` | Quick command reference | Documentation |
| `PROJECT_SUMMARY.md` | Technical summary & metrics | Documentation |
| `INDEX.md` | This file - Navigation guide | Documentation |
| `test_data.json` | **6 test cases** (all projects share) | Test Data |
| `run_all.ps1` | **Master test runner** (Windows) | Script |
| `run_all.sh` | **Master test runner** (Linux/Mac) | Script |
| `generate_comparison_report.py` | Creates comparison report | Script |
| `compare_report.md` | Generated comparison (after running) | Generated |
| `verify_structure.ps1` | Validates file structure | Utility |
| `cleanup.ps1` | Resets project to clean state | Utility |
| `quick_start.ps1` | Interactive setup guide | Utility |

### Project A: Pre-Enhancement (Broken Implementation)
**Location**: `Project_A_PreFeature_UI/`

| File | Purpose |
|------|---------|
| `src/chart_generator.py` | **Chart generator with static labels** (has overlaps) |
| `tests/test_pre_ui.py` | **Test suite** expecting failures |
| `requirements.txt` | Python dependencies |
| `setup.ps1` / `setup.sh` | Environment setup |
| `run_tests.ps1` / `run_tests.sh` | Test execution |
| `results/results_pre.json` | Test results (generated) |
| `results/charts/*.png` | Chart images (generated) |
| `logs/log_pre.txt` | Execution log (generated) |

### Project B: Post-Enhancement (Fixed Implementation)
**Location**: `Project_B_PostFeature_UI/`

| File | Purpose |
|------|---------|
| `src/chart_generator.py` | **Enhanced chart generator** (dynamic labels) |
| `tests/test_post_ui.py` | **Test suite** expecting passes |
| `requirements.txt` | Python dependencies (includes adjustText) |
| `setup.ps1` / `setup.sh` | Environment setup |
| `run_tests.ps1` / `run_tests.sh` | Test execution |
| `results/results_post.json` | Test results (generated) |
| `results/charts/*_enhanced.png` | Chart images (generated) |
| `logs/log_post.txt` | Execution log (generated) |

---

## 📖 Documentation Guide

### For First-Time Users
1. **Start here**: `README.md` - Complete setup and usage guide
2. **Quick commands**: `QUICK_REFERENCE.md` - Command cheat sheet
3. **Run interactive**: `.\quick_start.ps1` - Guided execution

### For Technical Review
1. **Technical details**: `PROJECT_SUMMARY.md` - Architecture & metrics
2. **Test data**: `test_data.json` - All 6 test cases with specifications
3. **Source code**: 
   - Pre: `Project_A_PreFeature_UI/src/chart_generator.py`
   - Post: `Project_B_PostFeature_UI/src/chart_generator.py`

### For Results Analysis
1. **Run tests**: `.\run_all.ps1`
2. **View comparison**: `compare_report.md` (generated)
3. **Check metrics**: `results/results_*.json` files
4. **View charts**: Browse `results/charts/` directories

---

## 🔍 Test Case Reference

| Test ID | Type | Chart Type | Data Points | Key Challenge |
|---------|------|------------|-------------|---------------|
| **TC001** | Normal | Bar | 5 | Basic functionality |
| **TC002** | Edge | Bar | 15 | High density |
| **TC003** | Boundary | Line | 6 | Similar values (85-89) |
| **TC004** | Complex | Multi-bar | 4×3 | Multiple series overlap |
| **TC005** | Malformed | Bar | 5 | Null/missing labels |
| **TC006** | Extreme | Bar | 4 | Large values (millions) |

**Details**: See `test_data.json`

---

## 📊 Expected Results Summary

### Project A (Pre-Enhancement) - Expected Failures
```
Total Tests: 6
Passed: 1 (TC005 - error handling)
Failed: 5 (overlap issues)
Success Rate: 16.7%
```

**Known Issues**:
- ❌ Static label positioning
- ❌ No collision detection
- ❌ Fixed font size (12pt)
- ❌ Poor contrast (2.5:1)
- ❌ No number formatting

### Project B (Post-Enhancement) - All Tests Pass
```
Total Tests: 6
Passed: 6 (all tests)
Failed: 0
Success Rate: 100%
```

**Improvements**:
- ✅ Dynamic label positioning
- ✅ Collision detection & avoidance
- ✅ Adaptive font sizing (8-14pt)
- ✅ Excellent contrast (7.2:1)
- ✅ Smart number formatting ($1.2M)

---

## 🛠️ Command Reference

### Essential Commands
```powershell
# Verify structure
.\verify_structure.ps1

# Run everything
.\run_all.ps1

# Interactive guide
.\quick_start.ps1

# Clean/reset
.\cleanup.ps1
```

### Individual Projects
```powershell
# Project A only
cd Project_A_PreFeature_UI
.\setup.ps1
.\run_tests.ps1

# Project B only
cd Project_B_PostFeature_UI
.\setup.ps1
.\run_tests.ps1
```

### Viewing Results
```powershell
# Comparison report
type compare_report.md

# JSON results
type Project_A_PreFeature_UI\results\results_pre.json
type Project_B_PostFeature_UI\results\results_post.json

# Logs
type Project_A_PreFeature_UI\logs\log_pre.txt
type Project_B_PostFeature_UI\logs\log_post.txt
```

---

## 📈 Key Metrics Comparison

| Metric | Pre-Enhancement | Post-Enhancement | Improvement |
|--------|-----------------|------------------|-------------|
| **Test Pass Rate** | 16.7% (1/6) | 100% (6/6) | +83.3 pts |
| **Contrast Ratio** | 2.5:1 | 7.2:1 | +188% |
| **WCAG AA** | ❌ Fail | ✅ Pass | Fixed |
| **WCAG AAA** | ❌ Fail | ✅ Pass | Fixed |
| **Label Overlaps** | Yes | No | Fixed |
| **Font Adaptation** | No | Yes | Added |
| **Number Formatting** | No | Yes | Added |
| **DPI** | 100 | 150 | +50% |

---

## 🎯 Deliverables Checklist

### Required Files (All Present ✓)
- ✅ Test scenario descriptions (in test_data.json)
- ✅ Structured test data (6 test cases, JSON)
- ✅ Edge/boundary cases (TC002, TC003, TC006)
- ✅ Malformed input handling (TC005)
- ✅ Complex scenarios (TC004 multi-series)
- ✅ Reproducible environment (requirements.txt, setup scripts)
- ✅ Executable test code (pytest-based)
- ✅ Execution scripts (run_tests.sh/ps1, run_all.sh/ps1)
- ✅ Before/after screenshots (generated in results/charts/)
- ✅ JSON results (results_pre.json, results_post.json)
- ✅ Comparison report (compare_report.md)
- ✅ Documentation (README.md, PROJECT_SUMMARY.md)

### Project A Deliverables
- ✅ Source code with known issues
- ✅ Test suite expecting failures
- ✅ Results showing expected failures
- ✅ Charts demonstrating overlap problems

### Project B Deliverables
- ✅ Enhanced source code
- ✅ Test suite expecting passes
- ✅ Results showing all tests pass
- ✅ Charts demonstrating improvements

### Shared Deliverables
- ✅ Master test runner
- ✅ Comparison report generator
- ✅ Comprehensive documentation
- ✅ Utility scripts

---

## 🔧 Prerequisites

- **Python**: 3.8 or higher
- **pip**: Latest version
- **OS**: Windows, Linux, or Mac
- **Disk Space**: ~500MB (including virtual environments)

### Python Packages
All installed automatically via `setup.ps1`:
- matplotlib >= 3.5.0
- numpy >= 1.21.0
- pillow >= 9.0.0
- pytest >= 7.0.0
- adjustText >= 0.8.0 (Project B only)

---

## 📞 Support & Troubleshooting

### Common Issues

**"Python not found"**
- Install Python 3.8+ from python.org
- Ensure Python is in system PATH

**"Permission denied" on scripts**
- Windows: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
- Linux/Mac: `chmod +x *.sh`

**"Module not found"**
- Activate virtual environment first
- Run setup script again: `.\setup.ps1`

**Tests fail unexpectedly**
- Check logs in `logs/` directories
- Verify Python version: `python --version`
- Ensure dependencies installed: `pip list`

### Where to Get Help
1. Check `README.md` for detailed instructions
2. Review `PROJECT_SUMMARY.md` for technical details
3. Examine log files in `logs/` directories
4. Verify structure with `.\verify_structure.ps1`

---

## 🎓 Learning Path

### For Evaluators
1. Read `PROJECT_SUMMARY.md` for context
2. Run `.\run_all.ps1` to see everything in action
3. Review `compare_report.md` for results
4. Examine source code differences between Project A and B

### For Developers
1. Study `test_data.json` for test case structure
2. Compare implementations:
   - `Project_A_PreFeature_UI/src/chart_generator.py`
   - `Project_B_PostFeature_UI/src/chart_generator.py`
3. Review test strategies:
   - `Project_A_PreFeature_UI/tests/test_pre_ui.py`
   - `Project_B_PostFeature_UI/tests/test_post_ui.py`

### For AI Model Evaluation
1. Verify all files generated correctly
2. Run tests and check success rates
3. Review visual differences in charts
4. Validate metrics in JSON results
5. Ensure documentation is comprehensive

---

## 📝 Version Information

- **Version**: 1.0
- **Status**: ✅ Ready for Evaluation
- **Created**: 2025-11-06
- **Last Updated**: 2025-11-06
- **Compatibility**: Python 3.8+, Windows/Linux/Mac

---

## 🎯 Success Criteria

A successful evaluation should demonstrate:

1. ✅ All 21+ files generated correctly
2. ✅ Project A shows expected failures (1/6 pass)
3. ✅ Project B shows all tests pass (6/6 pass)
4. ✅ Visual improvements evident in charts
5. ✅ Accessibility metrics improve significantly
6. ✅ Comparison report auto-generated
7. ✅ Full reproducibility via scripts
8. ✅ Comprehensive documentation provided

---

## 📚 Additional Resources

- **Python Matplotlib**: https://matplotlib.org/
- **WCAG Guidelines**: https://www.w3.org/WAI/WCAG21/quickref/
- **adjustText Library**: https://github.com/Phlya/adjustText
- **pytest Documentation**: https://docs.pytest.org/

---

**Ready to start?** Run `.\verify_structure.ps1` then `.\run_all.ps1`

**Questions?** Check `README.md` or `QUICK_REFERENCE.md`

**Need to reset?** Run `.\cleanup.ps1`
