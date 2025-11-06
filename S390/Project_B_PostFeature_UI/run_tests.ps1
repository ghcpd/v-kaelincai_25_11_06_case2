# PowerShell version
python -m venv .venv
.\.venv\Scripts\Activate.ps1; pip install --upgrade pip; pip install -r requirements.txt
pytest -q tests --maxfail=1 --disable-warnings
Copy-Item -Path (Get-ChildItem -Path . -Filter results_post.json -Recurse | Select-Object -First 1).FullName -Destination results
Get-ChildItem -Path . -Filter chart_post_*.png -Recurse | Select-Object -First 10 | ForEach-Object { Copy-Item $_.FullName -Destination results }
