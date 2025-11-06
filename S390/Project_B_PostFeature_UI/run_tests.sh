#!/usr/bin/env bash
set -e
python -m venv .venv
. .venv/Scripts/activate; pip install --upgrade pip; pip install -r requirements.txt
PYTHONPATH=$PWD python -m pytest -q tests --maxfail=1 --disable-warnings
cp $(find . -name 'results_post.json' | head -n 1) results/results_post.json || true
cp -r $(find . -name 'chart_post_*.png' | head -n 10) results/ || true
