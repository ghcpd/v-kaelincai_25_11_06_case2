# Master Test Execution Script (Windows PowerShell)
# Runs both Project A and Project B tests, then generates comparison report

Write-Host ""
Write-Host "============================================================" -ForegroundColor Magenta
Write-Host "  Data Visualization Enhancement - Full Test Suite" -ForegroundColor Magenta
Write-Host "============================================================" -ForegroundColor Magenta
Write-Host ""

$ErrorActionPreference = "Continue"
$StartTime = Get-Date

# ============================================================
# Step 1: Setup and Run Project A (Pre-Enhancement)
# ============================================================

Write-Host "STEP 1: Setting up Project A (Pre-Enhancement)..." -ForegroundColor Cyan
Write-Host "------------------------------------------------------------" -ForegroundColor Gray

Set-Location "Project_A_PreFeature_UI"

# Setup environment
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment for Project A..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate and install dependencies
& .\venv\Scripts\Activate.ps1
pip install --upgrade pip -q
pip install -r requirements.txt -q

Write-Host "Running Project A tests..." -ForegroundColor Yellow
Write-Host ""

# Run tests
& .\run_tests.ps1

Set-Location ..

Write-Host ""
Write-Host "Project A testing complete!" -ForegroundColor Green
Write-Host ""

# ============================================================
# Step 2: Setup and Run Project B (Post-Enhancement)
# ============================================================

Write-Host "STEP 2: Setting up Project B (Post-Enhancement)..." -ForegroundColor Cyan
Write-Host "------------------------------------------------------------" -ForegroundColor Gray

Set-Location "Project_B_PostFeature_UI"

# Setup environment
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment for Project B..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate and install dependencies
& .\venv\Scripts\Activate.ps1
pip install --upgrade pip -q
pip install -r requirements.txt -q

Write-Host "Running Project B tests..." -ForegroundColor Yellow
Write-Host ""

# Run tests
& .\run_tests.ps1

Set-Location ..

Write-Host ""
Write-Host "Project B testing complete!" -ForegroundColor Green
Write-Host ""

# ============================================================
# Step 3: Generate Comparison Report
# ============================================================

Write-Host "STEP 3: Generating comparison report..." -ForegroundColor Cyan
Write-Host "------------------------------------------------------------" -ForegroundColor Gray

python generate_comparison_report.py

Write-Host ""
Write-Host "Comparison report generated!" -ForegroundColor Green
Write-Host ""

# ============================================================
# Summary
# ============================================================

$EndTime = Get-Date
$Duration = $EndTime - $StartTime

Write-Host ""
Write-Host "============================================================" -ForegroundColor Magenta
Write-Host "  ALL TESTS COMPLETED SUCCESSFULLY" -ForegroundColor Magenta
Write-Host "============================================================" -ForegroundColor Magenta
Write-Host ""
Write-Host "Execution Time: $($Duration.ToString('mm\:ss'))" -ForegroundColor White
Write-Host ""
Write-Host "Results Location:" -ForegroundColor Yellow
Write-Host "  - Project A Results: Project_A_PreFeature_UI\results\" -ForegroundColor White
Write-Host "  - Project B Results: Project_B_PostFeature_UI\results\" -ForegroundColor White
Write-Host "  - Comparison Report: compare_report.md" -ForegroundColor White
Write-Host ""
Write-Host "Charts Location:" -ForegroundColor Yellow
Write-Host "  - Pre-Enhancement:  Project_A_PreFeature_UI\results\charts\" -ForegroundColor White
Write-Host "  - Post-Enhancement: Project_B_PostFeature_UI\results\charts\" -ForegroundColor White
Write-Host ""
Write-Host "To view the comparison report, open: compare_report.md" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Magenta
Write-Host ""
