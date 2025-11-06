#!/usr/bin/env bash
set -e
PYTHONPATH=. pytest -q Project_B_PostFeature_UI/tests/test_post_ui.py | tee Project_B_PostFeature_UI/logs/log_post.txt
