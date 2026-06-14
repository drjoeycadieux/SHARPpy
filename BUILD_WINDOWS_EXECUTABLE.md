# Complete Windows Executable Build Guide for SHARPpy

## Overview

This guide explains how to create a standalone Windows executable for SHARPpy that can run on any Windows 10/11 machine without requiring Python installation.

## System Requirements

### To Build the Executable
- **Operating System**: Windows 10 or Windows 11
- **Anaconda/Miniconda**: Download from https://www.anaconda.com/products/individual
- **Disk Space**: ~2-3 GB (for conda environment + build output)
- **Internet**: Required for downloading dependencies (first time only)
- **Time**: 5-15 minutes on first build, 1-2 minutes on subsequent builds

### To Run the Executable
- **Operating System**: Windows 7 SP1 or later (10/11 recommended)
- **Disk Space**: ~400 MB
- **No Python installation required!**

## Quick Start (Recommended)

### Step 1: Get SHARPpy

**Option A: Download ZIP**
1. Go to https://github.com/sharppy/SHARPpy
2. Click "Code" → "Download ZIP"
3. Extract to a folder (e.g., `C:\SHARPpy`)

**Option B: Clone with Git**
```cmd
git clone https://github.com/sharppy/SHARPpy
cd SHARPpy
```

### Step 2: Build the Executable

1. **Open Anaconda Prompt**
   - Search for "Anaconda Prompt" in Windows Start menu
   - Right-click and select "Run as Administrator" (recommended)

2. **Navigate to SHARPpy folder**
   ```cmd
   cd C:\path\to\SHARPpy
   ```

3. **Run the build script**
   ```cmd
   build_windows_exe.bat
   ```

4. **Wait for completion** - The script will:
   - Create a conda environment
   - Install all dependencies
   - Build the executable
   - Verify success

### Step 3: Run SHARPpy

The executable is in one of two locations:

**Option 1: If single file was created**
```
C:\SHARPpy\dist\SHARPpy.exe
```

**Option 2: If folder was created**
```
C:\SHARPpy\dist\SHARPpy\SHARPpy.exe
```

Double-click to run!

## Advanced Usage

### Building from Command Line (Manual)

If the batch script doesn't work:

```cmd
:: Create environment
conda env create -f environment.yml

:: Activate environment
conda activate devel

:: Install SHARPpy
python setup.py install

:: Navigate to runsharp directory
cd runsharp

:: Build executable
pyinstaller SHARPpy-win.spec
```

Then find the executable in `dist\SHARPpy.exe` or `dist\SHARPpy\SHARPpy.exe`

### Using PowerShell

```powershell
# If you see execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser

# Then run:
.\build_windows_exe.ps1
```

### Creating a Single-File Executable

The default creates a folder with many files. For a single `.exe` file:

```cmd
cd runsharp
pyinstaller SHARPpy-win.spec --onefile
```

**Trade-offs:**
- **Folder version**: Smaller download, faster startup
- **Single-file version**: Easier to share, slower first startup

### Using the Improved Spec File

There's an improved version with better error handling:

```cmd
cd runsharp
pyinstaller SHARPpy-win-improved.spec
```

## Creating an Installer

To create a professional `.msi` installer:

1. **Install NSIS** (Nullsoft Scriptable Install System)
   - Download from: http://nsis.sourceforge.net/
   - Run the installer

2. **Create an NSIS script** in `dist/` folder named `installer.nsi`:

```nsis
; SHARPpy Installer Script
!include "MUI2.nsh"

!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Name "SHARPpy"
OutFile "SHARPpy-Installer.exe"
InstallDir "$PROGRAMFILES\SHARPpy"

Section "Install"
  SetOutPath "$INSTDIR"
  File /r "SHARPpy\*.*"
  CreateShortCut "$SMPROGRAMS\SHARPpy.lnk" "$INSTDIR\SHARPpy.exe"
  CreateShortCut "$DESKTOP\SHARPpy.lnk" "$INSTDIR\SHARPpy.exe"
SectionEnd
```

3. **Build the installer**
   - Right-click the `.nsi` file
   - Select "Compile NSIS Script"

## Troubleshooting

### "Anaconda Prompt not found"
- Install Anaconda from https://www.anaconda.com/
- Make sure to check "Add Anaconda to PATH" during installation
- Restart Windows after installation

### "conda not found"
- Open Anaconda Prompt instead of regular Command Prompt
- Or manually add Anaconda to PATH:
  1. Search for "Environment Variables" in Windows
  2. Click "Edit environment variables for your account"
  3. Click "New" under "User variables"
  4. Variable name: `PATH`
  5. Variable value: `C:\path\to\Anaconda3` (or `C:\path\to\Miniconda3`)
  6. Click OK and restart terminal

### "Permission Denied" (PowerShell)
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
.\build_windows_exe.ps1
```

### Build fails with "No module named X"
1. Delete the environment:
   ```cmd
   conda env remove -n devel
   ```

2. Run the build script again to recreate environment from scratch

### Build fails with "icon not found"
- The build will still succeed without an icon
- Or copy `icons/SHARPpy.ico` to the `runsharp/` directory

### "pyinstaller: command not found"
```cmd
conda activate devel
pip install pyinstaller
```

### The executable starts very slowly
- This is normal for PyInstaller executables on first run
- Run it again - it should be faster
- Single-file executables (`--onefile`) have slower startup times

## Tips for Success

1. **Use Administrator mode** when running Anaconda Prompt
2. **Use a fast internet connection** for first build
3. **Close other applications** to free up disk space
4. **Don't move the build folder** until complete
5. **Keep the conda environment** for rebuilding (much faster)

## Distribution

Once built, you can share the executable:

### Option 1: Single Executable File
- Share just `SHARPpy.exe`
- Users can put it anywhere and run it
- Size: ~300-400 MB

### Option 2: Folder with Files
- ZIP the entire `dist/SHARPpy/` folder
- Share the ZIP file
- Users extract and run `SHARPpy.exe`
- Smaller download, faster startup

### Option 3: Installer
- Create using NSIS (see above)
- Professional installation experience
- Users can uninstall like any Windows program

## Rebuilding

To rebuild after making code changes:

```cmd
cd runsharp
pyinstaller SHARPpy-win.spec
```

Much faster because:
- Environment already exists
- Dependencies already downloaded
- Only code is rebuilt

## Getting Help

- **GitHub Issues**: https://github.com/sharppy/SHARPpy/issues
- **Documentation**: http://sharppy.github.io/SHARPpy/
- **Community**: Check existing issues for solutions

## Common Questions

**Q: Can I run the executable on non-Windows systems?**  
A: No, Windows executables only run on Windows. For macOS, use the OSX spec file.

**Q: How large is the executable?**  
A: ~200-400 MB depending on build options.

**Q: Is the executable slower than running from Python?**  
A: Startup is slightly slower, but runtime performance is the same.

**Q: Can I modify the source and rebuild quickly?**  
A: Yes! Just re-run `pyinstaller SHARPpy-win.spec` from the `runsharp/` folder.

**Q: What Python version is used?**  
A: Python 3.9 (specified in environment.yml)

**Q: Can I include in my own application?**  
A: Check the BSD license terms at https://github.com/sharppy/SHARPpy/blob/main/LICENSE.rst

## Version Information

- **SHARPpy**: See documentation for current version
- **Python**: 3.9
- **Build Tool**: PyInstaller
- **Last Updated**: 2024

For the latest information, visit: https://github.com/sharppy/SHARPpy
