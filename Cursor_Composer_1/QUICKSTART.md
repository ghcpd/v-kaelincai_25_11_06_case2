# Quick Start Guide

## Windows Users

### Step 1: Setup Projects
```powershell
# Setup Project A
cd Project_A_PreFeature_UI
.\setup.ps1
cd ..

# Setup Project B
cd Project_B_PostFeature_UI
.\setup.ps1
cd ..
```

### Step 2: Run All Tests
```powershell
.\run_all.ps1
```

This will:
- Run all tests for Project A (Pre-Enhancement)
- Run all tests for Project B (Post-Enhancement)
- Generate comparison report

### Step 3: View Results
- Test results: `Project_A_PreFeature_UI/results/results_pre.json` and `Project_B_PostFeature_UI/results/results_post.json`
- Charts: Check the `results/` folders in each project
- Comparison: `compare_report.md`

## Linux/macOS Users

### Step 1: Setup Projects
```bash
# Setup Project A
cd Project_A_PreFeature_UI
bash setup.sh
cd ..

# Setup Project B
cd Project_B_PostFeature_UI
bash setup.sh
cd ..

# Make scripts executable
chmod +x run_all.sh
chmod +x Project_*/run_tests.sh
```

### Step 2: Run All Tests
```bash
bash run_all.sh
```

## Manual Testing

### Test Project A Only
```powershell
# Windows
cd Project_A_PreFeature_UI
.\run_tests.ps1

# Linux/macOS
cd Project_A_PreFeature_UI
bash run_tests.sh
```

### Test Project B Only
```powershell
# Windows
cd Project_B_PostFeature_UI
.\run_tests.ps1

# Linux/macOS
cd Project_B_PostFeature_UI
bash run_tests.sh
```

## Expected Output

After running tests, you should see:
- ✅ Charts generated in `results/` directories
- ✅ JSON result files with test metrics
- ✅ Log files in `logs/` directories
- ✅ Comparison report at root level

## Troubleshooting

**Python not found:**
- Install Python 3.7+ from python.org
- Verify: `python --version`

**Module errors:**
- Run setup scripts to install dependencies
- Activate virtual environment: `.\venv\Scripts\Activate.ps1` (Windows) or `source venv/bin/activate` (Linux/macOS)

**Permission errors (Linux/macOS):**
- `chmod +x *.sh`

