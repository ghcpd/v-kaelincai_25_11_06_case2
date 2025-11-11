# Test execution script for Project B - Post-Enhancement (Windows PowerShell)

$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Running Project B - Post-Enhancement Tests" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment if it exists
if (Test-Path "venv\Scripts\Activate.ps1") {
    & .\venv\Scripts\Activate.ps1
}

# Ensure directories exist
New-Item -ItemType Directory -Force -Path results, logs | Out-Null

# Change to project directory
Set-Location $PSScriptRoot

# Run tests
Write-Host "Executing test suite..." -ForegroundColor Yellow
python tests\test_post_ui.py

# Check if results were generated
if (Test-Path "results\results_post.json") {
    Write-Host ""
    Write-Host "✓ Test results saved to results\results_post.json" -ForegroundColor Green
    Write-Host "✓ Charts generated in results\ directory" -ForegroundColor Green
    Write-Host "✓ Logs saved to logs\log_post.txt" -ForegroundColor Green
} else {
    Write-Host "Warning: Test results file not found" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Project B tests completed!" -ForegroundColor Green

