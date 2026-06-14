# SHARPpy Windows Build Instructions

## Quick Start

You need a **Windows 10/11 machine** with **Anaconda installed**.

### Using Automated Script (Recommended)

1. **Open Anaconda Prompt** (search in Windows Start menu)
2. **Navigate** to the SHARPpy folder:
   ```cmd
   cd C:\path\to\SHARPpy
   ```
3. **Run one of the build scripts**:
   - **Batch file** (Cmd/Command Prompt):
     ```cmd
     build_windows_exe.bat
     ```
   - **PowerShell** (if using PowerShell):
     ```powershell
     .\build_windows_exe.ps1
     ```

4. **Wait for completion** (5-15 minutes on first run)
5. **Find the executable** in the `dist\` folder

## The Executable

After successful build:
- **Location**: `dist\SHARPpy.exe` or `dist\SHARPpy\SHARPpy.exe`
- **Size**: ~200-400 MB
- **Portable**: Can run on any Windows machine without Python installation
- **Shareable**: Can be distributed to other users

## What the Scripts Do

1. Creates an isolated conda environment with all dependencies
2. Installs SHARPpy with all required packages
3. Runs PyInstaller to bundle everything into an executable
4. Verifies the build succeeded

## Troubleshooting

**"conda not found"**
- Make sure Anaconda/Miniconda is installed
- Run from Anaconda Prompt, not regular Command Prompt

**"Permission denied"** (PowerShell)
- Run PowerShell as Administrator
- Or run: `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser`

**Build fails with module errors**
- Delete the `devel` environment: `conda env remove -n devel`
- Run the script again to recreate it from scratch

## Manual Building

If automated scripts don't work:

```batch
conda env create -f environment.yml
conda activate devel
python setup.py install
cd runsharp
pyinstaller SHARPpy-win.spec
```

Then find the executable in `dist\SHARPpy.exe`

## Advanced Options

### Single-File Executable

Edit the `.spec` file to add `--onefile`:
```batch
pyinstaller SHARPpy-win.spec --onefile
```

This creates a single large EXE file instead of a folder.

### Creating an Installer

Use NSIS (http://nsis.sourceforge.net/) to package the `dist\SHARPpy` folder into a `.msi` installer.

## Support

- GitHub: https://github.com/sharppy/SHARPpy
- Issues: https://github.com/sharppy/SHARPpy/issues
- Docs: http://sharppy.github.io/SHARPpy/
