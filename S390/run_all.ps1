# PowerShell variant
$root = Get-Location
Push-Location Project_A_PreFeature_UI; Write-Output 'Running Project A tests...'; ./run_tests.ps1; Pop-Location
Push-Location Project_B_PostFeature_UI; Write-Output 'Running Project B tests...'; ./run_tests.ps1; Pop-Location
New-Item -ItemType Directory -Path shared\screenshots -Force | Out-Null
Copy-Item -Path Project_A_PreFeature_UI\results\*.png -Destination shared\screenshots -ErrorAction SilentlyContinue
Copy-Item -Path Project_B_PostFeature_UI\results\*.png -Destination shared\screenshots -ErrorAction SilentlyContinue
# Basic report
$A = Get-Content Project_A_PreFeature_UI\results\results_pre.json | ConvertFrom-Json
$B = Get-Content Project_B_PostFeature_UI\results\results_post.json | ConvertFrom-Json
@"
# Comparison Report

## Results Summary
- Project A tests: $($A.count)
- Project B tests: $($B.count)

## Detailed Results
### Pre-Feature Results
$(Get-Content Project_A_PreFeature_UI\results\results_pre.json)

### Post-Feature Results
$(Get-Content Project_B_PostFeature_UI\results\results_post.json)
"@> compare_report.md
Write-Output 'Report generated: compare_report.md'