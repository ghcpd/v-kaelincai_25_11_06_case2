# Quick Start Script for Data Visualization Enhancement Evaluation
# This script provides an interactive setup and execution guide

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Data Visualization Enhancement - Quick Start Guide" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "Checking prerequisites..." -ForegroundColor Yellow

try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Check pip
try {
    $pipVersion = pip --version 2>&1
    Write-Host "✓ pip found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ pip not found. Please install pip." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Prerequisites check complete!" -ForegroundColor Green
Write-Host ""

# Display menu
Write-Host "Please select an option:" -ForegroundColor Cyan
Write-Host ""
Write-Host "  1. Run Full Test Suite (Both Projects + Comparison)" -ForegroundColor White
Write-Host "  2. Run Project A Only (Pre-Enhancement)" -ForegroundColor White
Write-Host "  3. Run Project B Only (Post-Enhancement)" -ForegroundColor White
Write-Host "  4. Generate Comparison Report Only" -ForegroundColor White
Write-Host "  5. View README" -ForegroundColor White
Write-Host "  6. Exit" -ForegroundColor White
Write-Host ""

$choice = Read-Host "Enter your choice (1-6)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "Running full test suite..." -ForegroundColor Green
        Write-Host "This will take approximately 2-3 minutes." -ForegroundColor Yellow
        Write-Host ""
        & .\run_all.ps1
    }
    "2" {
        Write-Host ""
        Write-Host "Running Project A (Pre-Enhancement)..." -ForegroundColor Green
        Set-Location Project_A_PreFeature_UI
        & .\setup.ps1
        & .\run_tests.ps1
        Set-Location ..
    }
    "3" {
        Write-Host ""
        Write-Host "Running Project B (Post-Enhancement)..." -ForegroundColor Green
        Set-Location Project_B_PostFeature_UI
        & .\setup.ps1
        & .\run_tests.ps1
        Set-Location ..
    }
    "4" {
        Write-Host ""
        Write-Host "Generating comparison report..." -ForegroundColor Green
        python generate_comparison_report.py
        Write-Host ""
        Write-Host "Report generated: compare_report.md" -ForegroundColor Green
    }
    "5" {
        Write-Host ""
        Get-Content README.md | More
    }
    "6" {
        Write-Host ""
        Write-Host "Exiting..." -ForegroundColor Yellow
        exit 0
    }
    default {
        Write-Host ""
        Write-Host "Invalid choice. Exiting..." -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Quick Start Complete" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
