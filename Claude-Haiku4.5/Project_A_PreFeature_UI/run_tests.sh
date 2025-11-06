#!/bin/bash
# Test execution script for Project A - Pre-Enhancement

echo "=========================================="
echo "Running Project A - Pre-Enhancement Tests"
echo "=========================================="

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Create necessary directories
mkdir -p results/charts
mkdir -p logs

# Run tests and capture output
echo "Executing test suite..."
python -m pytest tests/test_pre_ui.py -v --tb=short 2>&1 | tee logs/log_pre.txt

# Also run the chart generator standalone
echo ""
echo "Generating charts..."
cd src
python chart_generator.py 2>&1 | tee -a ../logs/log_pre.txt
cd ..

echo ""
echo "=========================================="
echo "Test execution complete!"
echo "Results saved to: results/results_pre.json"
echo "Logs saved to: logs/log_pre.txt"
echo "Charts saved to: results/charts/"
echo "=========================================="
