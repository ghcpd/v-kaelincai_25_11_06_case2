#!/bin/bash
# Master Test Execution Script (Bash)
# Runs both Project A and Project B tests, then generates comparison report

echo ""
echo "============================================================"
echo "  Data Visualization Enhancement - Full Test Suite"
echo "============================================================"
echo ""

START_TIME=$(date +%s)

# ============================================================
# Step 1: Setup and Run Project A (Pre-Enhancement)
# ============================================================

echo "STEP 1: Setting up Project A (Pre-Enhancement)..."
echo "------------------------------------------------------------"

cd Project_A_PreFeature_UI

# Setup environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment for Project A..."
    python -m venv venv
fi

# Activate and install dependencies
source venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt -q

echo "Running Project A tests..."
echo ""

# Run tests
bash run_tests.sh

cd ..

echo ""
echo "Project A testing complete!"
echo ""

# ============================================================
# Step 2: Setup and Run Project B (Post-Enhancement)
# ============================================================

echo "STEP 2: Setting up Project B (Post-Enhancement)..."
echo "------------------------------------------------------------"

cd Project_B_PostFeature_UI

# Setup environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment for Project B..."
    python -m venv venv
fi

# Activate and install dependencies
source venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt -q

echo "Running Project B tests..."
echo ""

# Run tests
bash run_tests.sh

cd ..

echo ""
echo "Project B testing complete!"
echo ""

# ============================================================
# Step 3: Generate Comparison Report
# ============================================================

echo "STEP 3: Generating comparison report..."
echo "------------------------------------------------------------"

python generate_comparison_report.py

echo ""
echo "Comparison report generated!"
echo ""

# ============================================================
# Summary
# ============================================================

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

echo ""
echo "============================================================"
echo "  ALL TESTS COMPLETED SUCCESSFULLY"
echo "============================================================"
echo ""
echo "Execution Time: ${DURATION}s"
echo ""
echo "Results Location:"
echo "  - Project A Results: Project_A_PreFeature_UI/results/"
echo "  - Project B Results: Project_B_PostFeature_UI/results/"
echo "  - Comparison Report: compare_report.md"
echo ""
echo "Charts Location:"
echo "  - Pre-Enhancement:  Project_A_PreFeature_UI/results/charts/"
echo "  - Post-Enhancement: Project_B_PostFeature_UI/results/charts/"
echo ""
echo "To view the comparison report, open: compare_report.md"
echo "============================================================"
echo ""
