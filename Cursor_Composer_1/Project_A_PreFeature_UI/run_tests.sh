#!/bin/bash
# Test execution script for Project A - Pre-Enhancement

set -e

echo "=========================================="
echo "Running Project A - Pre-Enhancement Tests"
echo "=========================================="

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Ensure directories exist
mkdir -p results logs

# Change to project directory
cd "$(dirname "$0")"

# Run tests
echo "Executing test suite..."
python tests/test_pre_ui.py

# Check if results were generated
if [ -f "results/results_pre.json" ]; then
    echo ""
    echo "✓ Test results saved to results/results_pre.json"
    echo "✓ Charts generated in results/ directory"
    echo "✓ Logs saved to logs/log_pre.txt"
else
    echo "Warning: Test results file not found"
    exit 1
fi

echo ""
echo "Project A tests completed!"

