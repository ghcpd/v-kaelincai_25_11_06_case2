# Setup script for Project B - Post-Enhancement (Windows PowerShell)

Write-Host "Setting up Project B - Post-Enhancement Environment..." -ForegroundColor Green

# Create virtual environment if it doesn't exist
if (-not (Test-Path "venv")) {
    python -m venv venv
}

# Activate virtual environment
& .\venv\Scripts\Activate.ps1

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Environment setup complete!" -ForegroundColor Green
Write-Host "Virtual environment is now active."
