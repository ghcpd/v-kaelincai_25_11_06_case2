# Project Summary

## Overview

This repository contains a complete evaluation framework for assessing AI model capabilities in enhancing data visualization platforms. The evaluation focuses on improving chart readability through dynamic label positioning.

## Projects

### Project A - Pre-Enhancement
**Location**: `Project_A_PreFeature_UI/`

**Features**:
- Basic bar and line chart generation
- Static label positioning (above bars/points)
- No overlap detection or prevention
- Basic styling and contrast
- Labels remain fixed during chart updates

**Purpose**: Demonstrates the baseline implementation with known issues (overlapping labels).

### Project B - Post-Enhancement
**Location**: `Project_B_PostFeature_UI/`

**Features**:
- Enhanced bar and line chart generation
- Dynamic label positioning with overlap detection
- Improved readability (contrast, fonts, styling)
- Automatic label repositioning during updates
- Better accessibility features

**Purpose**: Demonstrates the enhanced implementation that addresses Project A's issues.

## Key Files

### Source Code
- `Project_A_PreFeature_UI/src/chart_generator.py` - Basic chart generator
- `Project_B_PostFeature_UI/src/chart_generator.py` - Enhanced chart generator with dynamic positioning

### Test Suites
- `Project_A_PreFeature_UI/tests/test_pre_ui.py` - Tests for baseline implementation
- `Project_B_PostFeature_UI/tests/test_post_ui.py` - Tests for enhanced implementation

### Test Data
- `test_data.json` - Shared test cases (6 test scenarios)
- Each project has a copy in its `data/` directory

### Execution Scripts
- `run_all.ps1` / `run_all.sh` - Master script to run all tests
- `Project_*/run_tests.ps1` / `Project_*/run_tests.sh` - Individual project test runners
- `Project_*/setup.ps1` / `Project_*/setup.sh` - Environment setup scripts

### Documentation
- `README.md` - Comprehensive documentation
- `QUICKSTART.md` - Quick start guide
- `compare_report.md` - Comparison report template (auto-generated after tests)

## Test Cases

1. **TC001**: Normal case - Basic bar chart
2. **TC002**: Edge case - Many data points (12 quarters)
3. **TC003**: Edge case - Very small values
4. **TC004**: Malformed input - Missing values (null handling)
5. **TC005**: Complex case - Multi-series line chart
6. **TC006**: Edge case - Very large values (millions)

## Key Improvements in Project B

1. **LabelOverlapDetector Class**: Detects and resolves label overlaps
2. **Dynamic Positioning**: Labels are repositioned to avoid collisions
3. **Enhanced Styling**: Better contrast, dynamic fonts, rounded boxes
4. **Update Handling**: Labels recalculate on data changes

## Technical Stack

- **Python 3.7+**
- **matplotlib** - Chart generation
- **numpy** - Numerical operations
- **Pillow (PIL)** - Image processing for tests

## Evaluation Metrics

Each test case evaluates:
- Label overlap detection
- Readability metrics
- Dynamic adjustment capability
- Error handling
- Multi-series support (where applicable)

## Output Artifacts

After running tests:
- **Charts**: PNG images in `results/` directories
- **Results**: JSON files with test metrics
- **Logs**: Execution logs in `logs/` directories
- **Report**: Comparison report with summary

## Usage

See `QUICKSTART.md` for detailed instructions.

Quick command:
```powershell
# Windows
.\run_all.ps1

# Linux/macOS
bash run_all.sh
```

## Project Status

✅ Complete and ready for evaluation
✅ All required files generated
✅ Test suites implemented
✅ Documentation provided
✅ Cross-platform scripts (Windows + Linux/macOS)

