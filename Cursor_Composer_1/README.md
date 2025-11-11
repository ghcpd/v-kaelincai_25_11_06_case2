# Data Visualization Enhancement Evaluation

## Overview

This repository contains two complete Python projects evaluating AI model capabilities for enhancing data visualization platforms. The evaluation focuses on improving chart readability by addressing label overlap issues and implementing dynamic label positioning.

**Project A (Pre-Enhancement)**: Basic charting implementation with static label positioning that results in overlapping labels.

**Project B (Post-Enhancement)**: Enhanced charting implementation with dynamic label positioning, improved readability, and better accessibility.

## Project Structure

```
.
├── Project_A_PreFeature_UI/          # Pre-enhancement project
│   ├── src/
│   │   └── chart_generator.py       # Basic chart generator
│   ├── tests/
│   │   └── test_pre_ui.py           # Test suite for Project A
│   ├── data/
│   │   └── test_data.json           # Test cases
│   ├── results/                      # Generated charts and results
│   ├── logs/                         # Execution logs
│   ├── requirements.txt
│   ├── setup.sh / setup.ps1
│   └── run_tests.sh / run_tests.ps1
│
├── Project_B_PostFeature_UI/         # Post-enhancement project
│   ├── src/
│   │   └── chart_generator.py       # Enhanced chart generator
│   ├── tests/
│   │   └── test_post_ui.py          # Test suite for Project B
│   ├── data/
│   │   └── test_data.json           # Test cases (same as Project A)
│   ├── results/                      # Generated charts and results
│   ├── logs/                         # Execution logs
│   ├── requirements.txt
│   ├── setup.sh / setup.ps1
│   └── run_tests.sh / run_tests.ps1
│
├── test_data.json                    # Shared test data
├── compare_report.md                 # Comparison report (generated)
├── run_all.sh / run_all.ps1          # Master execution script
└── README.md                         # This file
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## Quick Start

### Windows (PowerShell)

1. **Setup both projects:**
   ```powershell
   cd Project_A_PreFeature_UI
   .\setup.ps1
   cd ..\Project_B_PostFeature_UI
   .\setup.ps1
   cd ..
   ```

2. **Run all tests and generate comparison report:**
   ```powershell
   .\run_all.ps1
   ```

### Linux/macOS (Bash)

1. **Setup both projects:**
   ```bash
   cd Project_A_PreFeature_UI
   bash setup.sh
   cd ../Project_B_PostFeature_UI
   bash setup.sh
   cd ..
   ```

2. **Make scripts executable (if needed):**
   ```bash
   chmod +x run_all.sh
   chmod +x Project_A_PreFeature_UI/run_tests.sh
   chmod +x Project_B_PostFeature_UI/run_tests.sh
   ```

3. **Run all tests and generate comparison report:**
   ```bash
   bash run_all.sh
   ```

## Running Individual Projects

### Project A (Pre-Enhancement)

**Windows:**
```powershell
cd Project_A_PreFeature_UI
.\run_tests.ps1
```

**Linux/macOS:**
```bash
cd Project_A_PreFeature_UI
bash run_tests.sh
```

### Project B (Post-Enhancement)

**Windows:**
```powershell
cd Project_B_PostFeature_UI
.\run_tests.ps1
```

**Linux/macOS:**
```bash
cd Project_B_PostFeature_UI
bash run_tests.sh
```

## Test Cases

The evaluation includes 6 comprehensive test cases covering:

1. **TC001**: Normal case - Basic bar chart with readable labels
2. **TC002**: Edge case - Chart with many data points requiring dynamic adjustment
3. **TC003**: Edge case - Chart with very small values
4. **TC004**: Malformed input - Missing label values
5. **TC005**: Complex case - Multi-series chart with overlapping labels
6. **TC006**: Edge case - Chart with very large values

Each test case includes:
- Input data (labels and values)
- Expected behavior
- Pass/fail criteria
- Chart type specification

## Key Improvements in Project B

### 1. Dynamic Label Positioning
- **Problem (Project A)**: Labels are statically positioned above bars/points, causing overlaps
- **Solution (Project B)**: Labels are dynamically repositioned using an overlap detection algorithm that tries multiple positions (above, below, left, right) to avoid collisions

### 2. Enhanced Readability
- **Problem (Project A)**: Basic contrast and static font sizes
- **Solution (Project B)**: 
  - Improved color contrast (#2c3e50 text on white background)
  - Dynamic font sizing based on value magnitude
  - Enhanced visual styling with rounded label boxes

### 3. Dynamic Chart Updates
- **Problem (Project A)**: Labels remain in fixed positions when chart data changes
- **Solution (Project B)**: Labels are recalculated and repositioned whenever chart data is updated

### 4. Accessibility Improvements
- Better color contrast ratios
- Improved visual hierarchy
- Enhanced chart styling with cleaner design

## Test Results

After running the tests, you'll find:

- **Project A Results**: `Project_A_PreFeature_UI/results/results_pre.json`
- **Project B Results**: `Project_B_PostFeature_UI/results/results_post.json`
- **Comparison Report**: `compare_report.md` (auto-generated)
- **Charts**: PNG images in each project's `results/` directory
- **Logs**: Execution logs in each project's `logs/` directory

## Understanding the Results

### Results JSON Structure

Each results file contains:
```json
{
  "project": "Project_A_PreFeature_UI" or "Project_B_PostFeature_UI",
  "total_tests": <number>,
  "results": [
    {
      "test_id": "TC001",
      "description": "...",
      "status": "passed" | "failed" | "error",
      "metrics": {
        "overlap_detected": true/false,
        "readability": {...},
        "dynamic_adjustment": true/false
      },
      "chart_path": "path/to/chart.png"
    }
  ]
}
```

### Metrics Explained

- **overlap_detected**: Whether label overlaps were detected (expected `true` for Project A, `false` for Project B)
- **readability**: Readability metrics including contrast, font size, and image quality
- **dynamic_adjustment**: Whether labels are dynamically adjusted (expected `false` for Project A, `true` for Project B)

## Limitations and Future Improvements

### Current Limitations

1. **Overlap Detection**: The current overlap detection uses simplified heuristics. In production, consider:
   - OCR-based label detection
   - Advanced image analysis
   - Direct coordinate tracking during chart generation

2. **Label Positioning Algorithm**: The current algorithm tries a limited set of positions. Could be enhanced with:
   - Force-directed layout algorithms
   - Simulated annealing
   - Machine learning-based positioning

3. **Accessibility**: While improved, could add:
   - ARIA labels for screen readers
   - Keyboard navigation support
   - High contrast mode
   - Colorblind-friendly palettes

### Recommendations

1. **Performance Optimization**: For charts with many data points, consider:
   - Caching label positions
   - Incremental updates
   - Parallel processing

2. **User Preferences**: Allow users to configure:
   - Label positioning preferences
   - Font sizes
   - Color schemes

3. **Testing**: Expand test coverage with:
   - Visual regression tests
   - Performance benchmarks
   - Accessibility audits (WCAG 2.1 AA compliance)

## Troubleshooting

### Common Issues

1. **Python not found**
   - Ensure Python 3.7+ is installed and in PATH
   - Verify with: `python --version`

2. **Module not found errors**
   - Run setup scripts to install dependencies
   - Activate virtual environment: `.\venv\Scripts\Activate.ps1` (Windows) or `source venv/bin/activate` (Linux/macOS)

3. **Permission errors (Linux/macOS)**
   - Make scripts executable: `chmod +x *.sh`

4. **Chart generation fails**
   - Ensure matplotlib backend is properly configured
   - Check that output directories exist

## Contributing

This is an evaluation project. For improvements or bug fixes:

1. Document the issue or enhancement
2. Update test cases if needed
3. Ensure both projects are updated consistently
4. Update the comparison report

## License

This project is provided for evaluation purposes.

## Contact

For questions or issues related to this evaluation, please refer to the project documentation or create an issue in the repository.

