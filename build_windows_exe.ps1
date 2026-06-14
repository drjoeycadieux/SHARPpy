# PowerShell Build Script for SHARPpy
# This script automates the entire build process for creating a Windows executable
# Run this from: PowerShell in the SHARPpy root directory

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "===============================================" -ForegroundColor Green
Write-Host "   SHARPpy Windows Executable Builder" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Green
Write-Host ""

# Check if conda is available
try {
    $condaVersion = conda --version 2>$null
    Write-Host "[✓] Conda found: $condaVersion" -ForegroundColor Green
} catch {
    Write-Host "[✗] ERROR: Conda not found. Please install Anaconda and run this from PowerShell." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

try {
    # Step 1: Create/Update environment
    Write-Host "[1/5] Creating conda environment..." -ForegroundColor Yellow
    & conda env create -f environment.yml -y 2>&1 | Out-Null
    
    # Step 2: Activate environment
    Write-Host "[2/5] Activating environment..." -ForegroundColor Yellow
    $env:CONDA_PREFIX = $(conda run -n devel python -c "import sys; print(sys.prefix)")
    
    # Step 3: Install SHARPpy
    Write-Host "[3/5] Installing SHARPpy..." -ForegroundColor Yellow
    & conda run -n devel python setup.py install 2>&1 | Out-Null
    
    # Step 4: Build executable
    Write-Host "[4/5] Building Windows executable..." -ForegroundColor Yellow
    Write-Host "      This may take 5-15 minutes on first run..." -ForegroundColor Cyan
    Push-Location runsharp
    & conda run -n devel pyinstaller SHARPpy-win.spec
    Pop-Location
    
    # Step 5: Check for success
    Write-Host "[5/5] Finalizing build..." -ForegroundColor Yellow
    
    if (Test-Path "dist\SHARPpy.exe") {
        Write-Host ""
        Write-Host "===============================================" -ForegroundColor Green
        Write-Host "SUCCESS! Executable created successfully!" -ForegroundColor Green
        Write-Host "===============================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Location: $(Get-Item 'dist\SHARPpy.exe').FullName" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "You can:" -ForegroundColor Green
        Write-Host "  1. Run it directly: .\dist\SHARPpy.exe"
        Write-Host "  2. Create a shortcut to it"
        Write-Host "  3. Share it with others"
        Write-Host ""
    } elseif (Test-Path "dist\SHARPpy") {
        Write-Host ""
        Write-Host "===============================================" -ForegroundColor Green
        Write-Host "SUCCESS! Executable folder created!" -ForegroundColor Green
        Write-Host "===============================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Location: $(Get-Item 'dist\SHARPpy').FullName" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "The entire dist\SHARPpy folder contains all necessary files." -ForegroundColor Yellow
        Write-Host ""
    } else {
        throw "Executable not found in dist folder"
    }
    
    Write-Host "Build process complete!" -ForegroundColor Green
    
} catch {
    Write-Host ""
    Write-Host "✗ ERROR: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Check the console output above for details." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Read-Host "Press Enter to exit"
