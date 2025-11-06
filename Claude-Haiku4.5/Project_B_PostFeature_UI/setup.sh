#!/bin/bash
# Setup script for Project A - Pre-Enhancement

echo "Setting up Project A - Pre-Enhancement Environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Environment setup complete!"
echo "To activate the environment, run: source venv/bin/activate"
