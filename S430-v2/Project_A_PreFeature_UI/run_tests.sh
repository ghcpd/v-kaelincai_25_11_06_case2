#!/usr/bin/env bash
set -e
# install deps
python -m pip install -r requirements.txt
# run pytest
pytest -q Project_A_PreFeature_UI/tests | tee Project_A_PreFeature_UI/logs/log_pre.txt
