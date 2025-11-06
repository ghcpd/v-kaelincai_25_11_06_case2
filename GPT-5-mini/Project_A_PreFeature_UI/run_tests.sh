#!/usr/bin/env bash
set -e
PYTHONPATH=. pytest -q Project_A_PreFeature_UI/tests/test_pre_ui.py | tee Project_A_PreFeature_UI/logs/log_pre.txt
