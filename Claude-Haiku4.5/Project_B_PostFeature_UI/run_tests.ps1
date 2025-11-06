# Test execution script for Project B - Post-Enhancement (Windows PowerShell)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Running Project B - Post-Enhancement Tests" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# Activate virtual environment
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
}

# Create necessary directories
New-Item -ItemType Directory -Force -Path "results\charts" | Out-Null
New-Item -ItemType Directory -Force -Path "logs" | Out-Null

# Run tests and capture output
Write-Host "Executing test suite..." -ForegroundColor Yellow
python -m pytest tests\test_post_ui.py -v --tb=short 2>&1 | Tee-Object -FilePath "logs\log_post.txt"

# Also run the chart generator standalone
Write-Host ""
Write-Host "Generating enhanced charts..." -ForegroundColor Yellow
Set-Location src
python chart_generator.py 2>&1 | Tee-Object -FilePath "..\logs\log_post.txt" -Append
Set-Location ..

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "Test execution complete!" -ForegroundColor Green
Write-Host "Results saved to: results\results_post.json" -ForegroundColor White
Write-Host "Logs saved to: logs\log_post.txt" -ForegroundColor White
Write-Host "Charts saved to: results\charts\" -ForegroundColor White
Write-Host "==========================================" -ForegroundColor Green
