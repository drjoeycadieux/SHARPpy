# Building SHARPpy Windows Executable

This guide explains how to build a standalone Windows executable for SHARPpy.

## Prerequisites

You need:
1. **Windows 10/11** machine or VM
2. **Anaconda/Miniconda** (download from https://www.anaconda.com/products/individual)
3. **Git** (optional, for cloning the repo)

## Quick Start (Automated)

### Method 1: Using the Batch Script (Easiest)

1. **Clone or download** SHARPpy to your Windows machine
2. **Open Anaconda Prompt** (search for "Anaconda Prompt" in Windows Start menu)
3. **Navigate** to the SHARPpy folder:
   ```batch
   cd C:\path\to\SHARPpy
   ```
4. **Run the build script**:
   ```batch
   build_windows_exe.bat
   ```
5. The executable will be in the `dist\SHARPpy` folder

## Manual Build Process

### Step 1: Create the Environment

Open **Anaconda Prompt** and run:

```batch
cd C:\path\to\SHARPpy
conda env create -f environment.yml
conda activate devel
python setup.py install
```

### Step 2: Build the Executable

From the SHARPpy directory:

```batch
cd runsharp
pyinstaller SHARPpy-win.spec
```

### Step 3: Find Your Executable

The executable will be created in:
```
dist\SHARPpy.exe
```

You can also create a standalone version with:
```batch
pyinstaller SHARPpy-win.spec --onefile
```
This creates a single `SHARPpy.exe` file (larger but easier to distribute).

## Troubleshooting

### Issue: "pyinstaller not found"
- Make sure you've activated the conda environment: `conda activate devel`
- Reinstall pyinstaller: `pip install pyinstaller`

### Issue: Missing modules
- Ensure all dependencies are installed: `python setup.py install`
- If still failing, try: `pip install certifi requests python-dateutil`

### Issue: Icon not found
- Verify `icons\SHARPpy.ico` exists in the runsharp folder
- If missing, the build will still succeed but without the icon

## Creating an Installer (Optional)

To create a professional installer `.msi`, install NSIS after building the exe:

1. Download NSIS: http://nsis.sourceforge.net/
2. Create a configuration file and use NSIS to package the `dist\SHARPpy` folder

## Distribution

The built executable in `dist\SHARPpy\` (or `dist\SHARPpy.exe` if using `--onefile`) can be:
- Shared directly with users
- Packaged into a ZIP file for easy distribution
- Used to create an installer

## Notes

- First build takes 5-15 minutes (depending on system speed)
- Subsequent builds are faster
- The executable is self-contained and doesn't require Python installation on user machines
- File size is typically 200-400 MB

## Getting Help

- GitHub Issues: https://github.com/sharppy/SHARPpy/issues
- Documentation: http://sharppy.github.io/SHARPpy/index.html
