@echo off
REM Windows Build Script for SHARPpy
REM This script automates the entire build process for creating a Windows executable
REM Run this from: Anaconda Prompt in the SHARPpy root directory

setlocal enabledelayedexpansion

echo.
echo ===============================================
echo   SHARPpy Windows Executable Builder
echo ===============================================
echo.

REM Check if conda is available
where conda >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Conda not found. Please install Anaconda and run this from Anaconda Prompt.
    pause
    exit /b 1
)

REM Step 1: Create/Update environment
echo [1/5] Creating conda environment...
call conda env create -f environment.yml -y
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to create conda environment
    pause
    exit /b 1
)

REM Step 2: Activate environment
echo [2/5] Activating environment...
call conda activate devel
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate conda environment
    pause
    exit /b 1
)

REM Step 3: Install SHARPpy
echo [3/5] Installing SHARPpy...
call python setup.py install
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install SHARPpy
    pause
    exit /b 1
)

REM Step 4: Build executable
echo [4/5] Building Windows executable...
echo This may take 5-15 minutes on first run...
cd runsharp
call pyinstaller SHARPpy-win.spec
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: PyInstaller failed. Check console output above.
    pause
    exit /b 1
)
cd ..

REM Step 5: Package results
echo [5/5] Finalizing build...
if exist dist\SHARPpy.exe (
    echo.
    echo ===============================================
    echo SUCCESS! Executable created successfully!
    echo ===============================================
    echo.
    echo Location: dist\SHARPpy.exe
    echo.
    echo You can:
    echo   1. Run it directly: dist\SHARPpy.exe
    echo   2. Create a shortcut to it
    echo   3. Share it with others
    echo.
) else if exist dist\SHARPpy (
    echo.
    echo ===============================================
    echo SUCCESS! Executable folder created!
    echo ===============================================
    echo.
    echo Location: dist\SHARPpy\SHARPpy.exe
    echo.
    echo The entire dist\SHARPpy folder contains all necessary files.
    echo.
) else (
    echo ERROR: Executable not found in dist folder
    pause
    exit /b 1
)

echo Build process complete!
pause
