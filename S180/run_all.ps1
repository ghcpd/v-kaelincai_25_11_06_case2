Write-Host 'Running Project A tests...'
Push-Location Project_A_PreFeature_UI
.\setup.sh
.\run_tests.sh
Pop-Location
Write-Host 'Running Project B tests...'
Push-Location Project_B_PostFeature_UI
.\setup.sh
.\run_tests.sh
Pop-Location
Write-Host 'Copying results...'
New-Item -Path shared_artifacts -ItemType Directory -Force | Out-Null
Copy-Item -Path Project_A_PreFeature_UI\results\results_pre.json -Destination shared_artifacts -Force
Copy-Item -Path Project_B_PostFeature_UI\results\results_post.json -Destination shared_artifacts -Force
Write-Host 'Generate compare_report.json'
python shared_artifacts\create_compare_report.py
