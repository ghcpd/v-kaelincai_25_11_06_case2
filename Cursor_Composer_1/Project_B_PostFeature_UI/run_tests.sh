#!/bin/bash
# Test execution script for Project B - Post-Enhancement

set -e

echo "=========================================="
echo "Running Project B - Post-Enhancement Tests"
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
python tests/test_post_ui.py

# Check if results were generated
if [ -f "results/results_post.json" ]; then
    echo ""
    echo "✓ Test results saved to results/results_post.json"
    echo "✓ Charts generated in results/ directory"
    echo "✓ Logs saved to logs/log_post.txt"
else
    echo "Warning: Test results file not found"
    exit 1
fi

echo ""
echo "Project B tests completed!"

