#!/usr/bin/env bash
set -e
# Setup
python -m venv .venv
. .venv/Scripts/activate; pip install --upgrade pip; pip install -r requirements.txt
# Run tests
PYTHONPATH=$PWD python -m pytest -q tests --maxfail=1 --disable-warnings
# Collect results
cp $(find . -name 'results_pre.json' | head -n 1) results/results_pre.json || true
cp -r $(find . -name 'chart_pre_*.png' | head -n 10) results/ || true
