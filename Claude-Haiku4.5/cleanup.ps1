# Cleanup Script - Removes generated files and virtual environments
# Use this to reset the project to its initial state

Write-Host ""
Write-Host "============================================================" -ForegroundColor Yellow
Write-Host "  Project Cleanup Utility" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "This will remove:" -ForegroundColor Red
Write-Host "  - Virtual environments (venv folders)" -ForegroundColor White
Write-Host "  - Generated test results" -ForegroundColor White
Write-Host "  - Generated charts" -ForegroundColor White
Write-Host "  - Log files" -ForegroundColor White
Write-Host "  - Comparison report" -ForegroundColor White
Write-Host ""
Write-Host "Source code and test data will NOT be deleted." -ForegroundColor Green
Write-Host ""

$confirmation = Read-Host "Are you sure you want to continue? (yes/no)"

if ($confirmation -ne "yes") {
    Write-Host "Cleanup cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Starting cleanup..." -ForegroundColor Yellow
Write-Host ""

# Function to safely remove directory or file
function Remove-SafelyWithMessage {
    param($path, $description)
    if (Test-Path $path) {
        Remove-Item -Path $path -Recurse -Force -ErrorAction SilentlyContinue
        if (-not (Test-Path $path)) {
            Write-Host "✓ Removed: $description" -ForegroundColor Green
        } else {
            Write-Host "✗ Failed to remove: $description" -ForegroundColor Red
        }
    } else {
        Write-Host "○ Not found (already clean): $description" -ForegroundColor Gray
    }
}

# Clean Project A
Write-Host "Cleaning Project A..." -ForegroundColor Cyan
Remove-SafelyWithMessage "Project_A_PreFeature_UI\venv" "Project A virtual environment"
Remove-SafelyWithMessage "Project_A_PreFeature_UI\results" "Project A results"
Remove-SafelyWithMessage "Project_A_PreFeature_UI\logs" "Project A logs"
Remove-SafelyWithMessage "Project_A_PreFeature_UI\__pycache__" "Project A Python cache"
Remove-SafelyWithMessage "Project_A_PreFeature_UI\src\__pycache__" "Project A src cache"
Remove-SafelyWithMessage "Project_A_PreFeature_UI\tests\__pycache__" "Project A tests cache"
Remove-SafelyWithMessage "Project_A_PreFeature_UI\.pytest_cache" "Project A pytest cache"

Write-Host ""

# Clean Project B
Write-Host "Cleaning Project B..." -ForegroundColor Cyan
Remove-SafelyWithMessage "Project_B_PostFeature_UI\venv" "Project B virtual environment"
Remove-SafelyWithMessage "Project_B_PostFeature_UI\results" "Project B results"
Remove-SafelyWithMessage "Project_B_PostFeature_UI\logs" "Project B logs"
Remove-SafelyWithMessage "Project_B_PostFeature_UI\__pycache__" "Project B Python cache"
Remove-SafelyWithMessage "Project_B_PostFeature_UI\src\__pycache__" "Project B src cache"
Remove-SafelyWithMessage "Project_B_PostFeature_UI\tests\__pycache__" "Project B tests cache"
Remove-SafelyWithMessage "Project_B_PostFeature_UI\.pytest_cache" "Project B pytest cache"

Write-Host ""

# Clean root
Write-Host "Cleaning root directory..." -ForegroundColor Cyan
Remove-SafelyWithMessage "compare_report.md" "Comparison report"
Remove-SafelyWithMessage "__pycache__" "Root Python cache"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  Cleanup Complete!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Project is now reset to initial state." -ForegroundColor White
Write-Host "Run .\run_all.ps1 to regenerate all results." -ForegroundColor Yellow
Write-Host ""
