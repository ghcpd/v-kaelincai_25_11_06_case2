#!/bin/bash
# Test execution script for Project B - Post-Enhancement

echo "=========================================="
echo "Running Project B - Post-Enhancement Tests"
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
python -m pytest tests/test_post_ui.py -v --tb=short 2>&1 | tee logs/log_post.txt

# Also run the chart generator standalone
echo ""
echo "Generating enhanced charts..."
cd src
python chart_generator.py 2>&1 | tee -a ../logs/log_post.txt
cd ..

echo ""
echo "=========================================="
echo "Test execution complete!"
echo "Results saved to: results/results_post.json"
echo "Logs saved to: logs/log_post.txt"
echo "Charts saved to: results/charts/"
echo "=========================================="
