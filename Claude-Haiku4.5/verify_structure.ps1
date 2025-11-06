# Project Structure Verification Script
# Validates that all required files and directories are present

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Project Structure Verification" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

$allGood = $true

function Test-FileExists {
    param($path, $description)
    if (Test-Path $path) {
        Write-Host "✓ $description" -ForegroundColor Green
        return $true
    } else {
        Write-Host "✗ $description" -ForegroundColor Red
        return $false
    }
}

# Root files
Write-Host "Checking root files..." -ForegroundColor Yellow
$allGood = (Test-FileExists "test_data.json" "Shared test data") -and $allGood
$allGood = (Test-FileExists "README.md" "Main README") -and $allGood
$allGood = (Test-FileExists "PROJECT_SUMMARY.md" "Project summary") -and $allGood
$allGood = (Test-FileExists "generate_comparison_report.py" "Report generator") -and $allGood
$allGood = (Test-FileExists "run_all.ps1" "Master runner (PowerShell)") -and $allGood
$allGood = (Test-FileExists "run_all.sh" "Master runner (Bash)") -and $allGood
$allGood = (Test-FileExists "quick_start.ps1" "Quick start script") -and $allGood
Write-Host ""

# Project A files
Write-Host "Checking Project A (Pre-Enhancement)..." -ForegroundColor Yellow
$allGood = (Test-FileExists "Project_A_PreFeature_UI\src\chart_generator.py" "Project A source code") -and $allGood
$allGood = (Test-FileExists "Project_A_PreFeature_UI\tests\test_pre_ui.py" "Project A tests") -and $allGood
$allGood = (Test-FileExists "Project_A_PreFeature_UI\requirements.txt" "Project A requirements") -and $allGood
$allGood = (Test-FileExists "Project_A_PreFeature_UI\setup.ps1" "Project A setup (PowerShell)") -and $allGood
$allGood = (Test-FileExists "Project_A_PreFeature_UI\setup.sh" "Project A setup (Bash)") -and $allGood
$allGood = (Test-FileExists "Project_A_PreFeature_UI\run_tests.ps1" "Project A test runner (PowerShell)") -and $allGood
$allGood = (Test-FileExists "Project_A_PreFeature_UI\run_tests.sh" "Project A test runner (Bash)") -and $allGood
Write-Host ""

# Project B files
Write-Host "Checking Project B (Post-Enhancement)..." -ForegroundColor Yellow
$allGood = (Test-FileExists "Project_B_PostFeature_UI\src\chart_generator.py" "Project B source code") -and $allGood
$allGood = (Test-FileExists "Project_B_PostFeature_UI\tests\test_post_ui.py" "Project B tests") -and $allGood
$allGood = (Test-FileExists "Project_B_PostFeature_UI\requirements.txt" "Project B requirements") -and $allGood
$allGood = (Test-FileExists "Project_B_PostFeature_UI\setup.ps1" "Project B setup (PowerShell)") -and $allGood
$allGood = (Test-FileExists "Project_B_PostFeature_UI\setup.sh" "Project B setup (Bash)") -and $allGood
$allGood = (Test-FileExists "Project_B_PostFeature_UI\run_tests.ps1" "Project B test runner (PowerShell)") -and $allGood
$allGood = (Test-FileExists "Project_B_PostFeature_UI\run_tests.sh" "Project B test runner (Bash)") -and $allGood
Write-Host ""

# Summary
Write-Host "============================================================" -ForegroundColor Cyan
if ($allGood) {
    Write-Host "  ALL FILES VERIFIED - STRUCTURE COMPLETE ✓" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Ready to run! Execute: .\run_all.ps1" -ForegroundColor Yellow
} else {
    Write-Host "  MISSING FILES DETECTED - STRUCTURE INCOMPLETE ✗" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Please ensure all files are present before running tests." -ForegroundColor Yellow
}
Write-Host ""

# Count test cases
Write-Host "Test Data Statistics:" -ForegroundColor Cyan
try {
    $testData = Get-Content "test_data.json" | ConvertFrom-Json
    $testCount = $testData.test_cases.Count
    Write-Host "  Total test cases: $testCount" -ForegroundColor White
    Write-Host "  Normal cases: $($testData.metadata.normal_cases)" -ForegroundColor White
    Write-Host "  Edge cases: $($testData.metadata.edge_cases)" -ForegroundColor White
    Write-Host "  Malformed cases: $($testData.metadata.malformed_cases)" -ForegroundColor White
} catch {
    Write-Host "  Could not read test_data.json" -ForegroundColor Red
}

Write-Host ""
