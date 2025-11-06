# Data Visualization Enhancement Evaluation

## Overview

This repository contains two complete Python projects designed to evaluate AI models' ability to implement enhancements in data visualization platforms. The projects demonstrate improvements in chart readability through dynamic label positioning and accessibility enhancements.

### Projects Included

1. **Project A - Pre-Enhancement (Basic Implementation)**
   - Located in: `Project_A_PreFeature_UI/`
   - Contains the original implementation with overlapping label issues
   - Demonstrates static label positioning problems

2. **Project B - Post-Enhancement (Improved Implementation)**
   - Located in: `Project_B_PostFeature_UI/`
   - Contains the enhanced implementation with dynamic label positioning
   - Demonstrates accessibility and readability improvements

## Key Features

### Pre-Enhancement Issues (Project A)
- ❌ Static label positioning causing overlaps
- ❌ Fixed font size regardless of chart density
- ❌ No dynamic adjustment for chart updates
- ❌ Poor contrast and accessibility scores
- ❌ Long numbers without formatting

### Post-Enhancement Improvements (Project B)
- ✅ Dynamic label positioning with collision detection
- ✅ Adaptive font sizing based on data density
- ✅ Smart number formatting (K, M abbreviations)
- ✅ WCAG AAA compliant contrast ratios (7:1)
- ✅ Intelligent multi-series label staggering
- ✅ Background boxes for improved readability
- ✅ adjustText library integration for optimization
- ✅ Higher DPI rendering (150 vs 100)

## Test Coverage

The test suite includes 6 comprehensive test cases:

| Test ID | Type | Description |
|---------|------|-------------|
| TC001 | Normal | Basic bar chart with 5 data points |
| TC002 | Edge | High-density chart with 15 data points |
| TC003 | Boundary | Line chart with clustered similar values |
| TC004 | Complex | Multi-series bar chart with 3 series |
| TC005 | Malformed | Missing/null label values |
| TC006 | Extreme | Very large values requiring formatting |

## Directory Structure

```
chatWorkspace/
├── Project_A_PreFeature_UI/          # Pre-Enhancement Version
│   ├── src/
│   │   └── chart_generator.py        # Basic chart generator
│   ├── tests/
│   │   └── test_pre_ui.py           # Test suite for pre-enhancement
│   ├── results/
│   │   ├── charts/                   # Generated chart images
│   │   └── results_pre.json         # Test results
│   ├── logs/
│   │   └── log_pre.txt              # Execution logs
│   ├── requirements.txt              # Python dependencies
│   ├── setup.ps1                     # Windows setup script
│   ├── setup.sh                      # Linux/Mac setup script
│   ├── run_tests.ps1                 # Windows test runner
│   └── run_tests.sh                  # Linux/Mac test runner
│
├── Project_B_PostFeature_UI/         # Post-Enhancement Version
│   ├── src/
│   │   └── chart_generator.py        # Enhanced chart generator
│   ├── tests/
│   │   └── test_post_ui.py          # Test suite for post-enhancement
│   ├── results/
│   │   ├── charts/                   # Generated chart images
│   │   └── results_post.json        # Test results
│   ├── logs/
│   │   └── log_post.txt             # Execution logs
│   ├── requirements.txt              # Python dependencies
│   ├── setup.ps1                     # Windows setup script
│   ├── setup.sh                      # Linux/Mac setup script
│   ├── run_tests.ps1                 # Windows test runner
│   └── run_tests.sh                  # Linux/Mac test runner
│
├── test_data.json                    # Shared test case definitions
├── generate_comparison_report.py     # Report generation script
├── compare_report.md                 # Generated comparison report
├── run_all.ps1                       # Master test runner (Windows)
├── run_all.sh                        # Master test runner (Linux/Mac)
└── README.md                         # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Python Dependencies

Both projects require:
- matplotlib >= 3.5.0
- numpy >= 1.21.0
- pillow >= 9.0.0
- pytest >= 7.0.0

Project B additionally requires:
- adjustText >= 0.8.0 (for advanced label positioning)

## Quick Start

### Option 1: Run Everything at Once (Recommended)

**Windows (PowerShell):**
```powershell
.\run_all.ps1
```

**Linux/Mac (Bash):**
```bash
chmod +x run_all.sh
./run_all.sh
```

This will:
1. Set up both project environments
2. Run all tests for Project A
3. Run all tests for Project B
4. Generate a comparison report with screenshots

### Option 2: Run Projects Individually

#### Project A (Pre-Enhancement)

**Windows:**
```powershell
cd Project_A_PreFeature_UI
.\setup.ps1
.\run_tests.ps1
```

**Linux/Mac:**
```bash
cd Project_A_PreFeature_UI
chmod +x setup.sh run_tests.sh
./setup.sh
./run_tests.sh
```

#### Project B (Post-Enhancement)

**Windows:**
```powershell
cd Project_B_PostFeature_UI
.\setup.ps1
.\run_tests.ps1
```

**Linux/Mac:**
```bash
cd Project_B_PostFeature_UI
chmod +x setup.sh run_tests.sh
./setup.sh
./run_tests.sh
```

## Understanding the Results

### Test Results Files

Each project generates a `results_*.json` file containing:
- Overall test statistics (passed/failed)
- Individual test case results
- Metrics and measurements
- Paths to generated chart images

**Example structure:**
```json
{
  "project": "Project A - Pre-Enhancement",
  "total_tests": 6,
  "passed": 1,
  "failed": 5,
  "test_results": [
    {
      "test_id": "TC001",
      "status": "FAIL",
      "issues": {
        "label_overlap": true,
        "poor_readability": true
      },
      "metrics": {
        "accessibility_score": 2.5
      }
    }
  ]
}
```

### Comparison Report

The `compare_report.md` file provides:
- Side-by-side test result comparison
- Before/after screenshots for each test case
- Quantitative improvement metrics
- Accessibility compliance analysis
- Executive summary with recommendations

### Chart Images

Generated charts are saved in:
- Pre-Enhancement: `Project_A_PreFeature_UI/results/charts/`
- Post-Enhancement: `Project_B_PostFeature_UI/results/charts/`

Naming convention: `{TEST_ID}_chart[_enhanced].png`

### Log Files

Execution logs are saved in:
- Pre-Enhancement: `Project_A_PreFeature_UI/logs/log_pre.txt`
- Post-Enhancement: `Project_B_PostFeature_UI/logs/log_post.txt`

## Key Metrics

### Accessibility Improvements

| Metric | Pre-Enhancement | Post-Enhancement | Standard |
|--------|-----------------|------------------|----------|
| Contrast Ratio | 2.5:1 | 7.2:1 | 4.5:1 (WCAG AA) |
| WCAG AA Compliance | ❌ Fail | ✅ Pass | Required |
| WCAG AAA Compliance | ❌ Fail | ✅ Pass | Recommended |
| Adaptive Font Sizing | ❌ No | ✅ Yes | Best Practice |

### Test Success Rates

| Project | Success Rate | Expected |
|---------|--------------|----------|
| Pre-Enhancement | ~16.7% (1/6) | Expected failures |
| Post-Enhancement | 100% (6/6) | All tests pass |

## Technical Implementation Details

### Pre-Enhancement (Project A)

The pre-enhancement version demonstrates common charting issues:

```python
# Static font size
self.default_font_size = 12

# Fixed offset for all labels
self.label_offset = 2

# No collision detection
ax.text(x, y + self.label_offset, value, fontsize=self.default_font_size)
```

### Post-Enhancement (Project B)

The enhanced version implements intelligent positioning:

```python
# Dynamic font sizing
def calculate_dynamic_font_size(self, num_elements):
    if num_elements <= 5:
        return 14
    elif num_elements <= 10:
        return 12
    else:
        return 8

# Collision detection and avoidance
def calculate_label_positions(self, values, base_positions, chart_height):
    positions = []
    for i, (value, base_y) in enumerate(zip(values, base_positions)):
        # Check for collisions and adjust
        # ... intelligent repositioning logic ...
    return positions

# adjustText library for final optimization
adjust_text(texts, only_move={'points': 'y', 'texts': 'y'})
```

## Interpreting Test Results

### Expected Outcomes

#### Project A (Pre-Enhancement)
- **TC001-TC004, TC006**: Expected to FAIL due to label overlap
- **TC005**: Expected to PASS (error handling works)
- Overall success rate: ~16.7%

#### Project B (Post-Enhancement)
- **All test cases**: Expected to PASS
- Overall success rate: 100%

### Success Criteria

A test case passes when:
1. ✅ Chart is successfully generated
2. ✅ No label overlaps detected
3. ✅ All labels are readable
4. ✅ Accessibility score ≥ 4.5 (WCAG AA)
5. ✅ Dynamic positioning is working
6. ✅ Appropriate font sizing for density

## Troubleshooting

### Common Issues

**1. Module not found errors**
```
Solution: Ensure virtual environment is activated and dependencies are installed
Windows: .\venv\Scripts\Activate.ps1
Linux/Mac: source venv/bin/activate
Then: pip install -r requirements.txt
```

**2. Permission denied on scripts**
```
Linux/Mac Solution: chmod +x *.sh
Windows Solution: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**3. Charts not displaying in report**
```
Solution: Ensure both projects have been run before generating the comparison report
The report uses relative paths to chart images
```

**4. Tests fail unexpectedly**
```
Solution: Check Python version (requires 3.8+)
Verify all dependencies are installed: pip list
Check logs in logs/ directory for detailed error messages
```

## Customization

### Adding New Test Cases

Edit `test_data.json` to add new test cases:

```json
{
  "test_id": "TC007",
  "name": "Your Test Name",
  "chart_type": "bar",
  "data": {
    "categories": ["A", "B", "C"],
    "values": [10, 20, 30],
    "title": "Test Chart"
  },
  "expected_behavior": {
    "label_overlap": false,
    "contrast_ratio_min": 4.5
  }
}
```

### Modifying Enhancement Parameters

In `Project_B_PostFeature_UI/src/chart_generator.py`:

```python
# Adjust minimum label spacing
self.min_label_spacing = 5  # pixels

# Change font size range
self.min_font_size = 8
self.max_font_size = 14

# Modify contrast color
def get_contrast_color(self):
    return '#1a1a1a'  # Very dark gray
```

## Evaluation Criteria

This project evaluates AI models on their ability to:

1. **Reproduce UI/UX Bugs**: Correctly implement the problematic pre-enhancement version
2. **Implement Enhancements**: Apply fixes that resolve the identified issues
3. **Automated Testing**: Create comprehensive test coverage
4. **Visual Evidence**: Generate before/after screenshots
5. **Quantitative Validation**: Measure improvements with concrete metrics
6. **Accessibility Compliance**: Meet WCAG standards
7. **Documentation**: Provide clear explanations and usage instructions

## Performance Benchmarks

Typical execution times (on standard hardware):

- Project A setup + tests: ~30-45 seconds
- Project B setup + tests: ~45-60 seconds
- Comparison report generation: ~2-5 seconds
- Total execution time: ~2-3 minutes

## Limitations and Future Improvements

### Current Limitations

1. Image-based overlap detection is simulated (not actual OCR)
2. Limited to bar, line, and multi-series bar charts
3. Contrast analysis is calculated, not measured from actual pixels
4. No interactive chart support

### Potential Enhancements

1. Implement actual OCR for label overlap detection
2. Add support for pie charts, scatter plots, and heatmaps
3. Real pixel-based contrast ratio calculation
4. Interactive chart generation with Plotly
5. Automated visual regression testing
6. Performance profiling for large datasets

## License

This project is provided for educational and evaluation purposes.

## Support

For issues or questions:
1. Check the logs in `logs/` directories
2. Review the comparison report for detailed analysis
3. Verify all prerequisites are met
4. Ensure Python 3.8+ is installed

## Acknowledgments

This project uses the following open-source libraries:
- **Matplotlib**: Comprehensive plotting library
- **NumPy**: Numerical computing library
- **Pillow**: Image processing library
- **pytest**: Testing framework
- **adjustText**: Automatic text positioning

## Conclusion

This evaluation suite provides a comprehensive framework for testing AI models' ability to implement feature enhancements in data visualization systems. The side-by-side comparison clearly demonstrates the improvements in label positioning, readability, and accessibility compliance.

**Expected Outcome**: AI models should be able to:
- Generate both projects with all required files
- Demonstrate clear visual improvements in Project B
- Achieve 100% test pass rate in Project B
- Produce quantifiable accessibility improvements
- Generate comprehensive documentation

---

**Version**: 1.0  
**Last Updated**: 2025-11-06  
**Status**: Ready for Evaluation
