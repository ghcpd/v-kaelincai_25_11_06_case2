#!/usr/bin/env bash
set -e
python -m pip install -r requirements.txt
pytest -q Project_B_PostFeature_UI/tests | tee Project_B_PostFeature_UI/logs/log_post.txt
