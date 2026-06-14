# Windows Executable Build Checklist

Use this checklist to ensure everything is set up correctly before building.

## Pre-Build Checklist

### System & Environment
- [ ] Running Windows 10 or Windows 11
- [ ] Have at least 2-3 GB free disk space
- [ ] Have Anaconda or Miniconda installed
- [ ] Anaconda/Miniconda is in PATH (can type `conda` in Command Prompt)
- [ ] Using Anaconda Prompt (not regular Command Prompt)
- [ ] Preferably running Anaconda Prompt as Administrator

### Project Files
- [ ] SHARPpy repository downloaded or cloned
- [ ] Located at a path without spaces (or in a simple folder)
- [ ] `environment.yml` file exists in root
- [ ] `build_windows_exe.bat` file exists in root
- [ ] `runsharp/SHARPpy-win.spec` file exists
- [ ] `runsharp/SHARPpy.py` file exists

### Internet Connection
- [ ] Have a stable internet connection
- [ ] Download is at least 1 Mbps (for initial build)

## Build Checklist

### Before Running Build Script
- [ ] Closed IDE/code editor (optional but recommended)
- [ ] Closed other resource-intensive applications
- [ ] Anaconda Prompt is open and in `SHARPpy` root directory
- [ ] Not behind a restrictive corporate firewall/proxy (if issues occur)

### During Build
- [ ] Script shows progress messages
- [ ] No error messages appear in red
- [ ] conda environment is being created/updated
- [ ] PyInstaller is running and processing files
- [ ] Total time: 5-15 minutes on first run

## Post-Build Checklist

### Success Indicators
- [ ] Script shows "SUCCESS!" message
- [ ] One of these exists:
  - `dist\SHARPpy.exe` (single file)
  - `dist\SHARPpy\SHARPpy.exe` (folder version)
- [ ] Executable file size is > 100 MB
- [ ] No "ERROR" messages at end of build

### Executable Testing
- [ ] Can navigate to `dist\SHARPpy\` folder
- [ ] Can see `SHARPpy.exe` file
- [ ] Can double-click to launch (may take 10-30 seconds on first run)
- [ ] Application window opens successfully
- [ ] Can use the GUI (load data, interact, etc.)

## Troubleshooting Checklist

If build fails, check these:

### Build Script Issues
- [ ] Ran script from correct directory (SHARPpy root)
- [ ] Using Anaconda Prompt (not regular Command Prompt)
- [ ] No typos in command
- [ ] File names and paths don't have unusual characters

### Conda Issues
- [ ] Conda is installed (type `conda --version`)
- [ ] Internet connection is stable
- [ ] Anaconda is up to date: `conda update conda`
- [ ] Conda base environment isn't corrupted: `conda info`

### Permission Issues
- [ ] Running as Administrator
- [ ] Windows Defender isn't blocking file operations
- [ ] Check antivirus isn't interfering with build
- [ ] User account has write permissions to folder

### Disk Space Issues
- [ ] Have at least 3 GB free on drive
- [ ] Temp folders aren't full (`C:\Users\[user]\AppData\Local\Temp`)
- [ ] Try cleaning up with Disk Cleanup utility

### Module/Dependency Issues
- [ ] Delete conda environment and rebuild:
  ```cmd
  conda env remove -n devel
  build_windows_exe.bat
  ```
- [ ] Check Python version: `python --version` (should be 3.9)
- [ ] Verify all packages: `pip list`

## Success Verification

Once build completes, verify the executable works:

```cmd
:: Test from command line
dist\SHARPpy\SHARPpy.exe

:: Or navigate to dist\ and double-click SHARPpy.exe
```

Expected behavior:
1. 10-30 second startup delay (first time)
2. SHARPpy window appears
3. No error messages in console
4. Can load data and use interface

## Distribution Checklist

If sharing the executable:

### Folder Version (Recommended)
- [ ] Copy entire `dist\SHARPpy\` folder
- [ ] Create ZIP file: `SHARPpy-Portable.zip`
- [ ] Test ZIP extraction and running on clean Windows machine
- [ ] Include README with instructions to extract and run

### Single-File Version
- [ ] Only `dist\SHARPpy.exe` is needed
- [ ] File size should be 300-400 MB
- [ ] Share with clear instructions (run directly, no extraction needed)

### Installation Package
- [ ] NSIS script created and compiled to `.msi`
- [ ] Test installer on clean Windows machine
- [ ] Verify uninstall works correctly
- [ ] Create installer installer with clear instructions

## Performance Tuning

To improve build performance:

- [ ] Enable UPX (already enabled in spec file)
- [ ] Close other applications during build
- [ ] Use SSD if available (much faster builds)
- [ ] For second builds, build is 5-10x faster (environment exists)

## Additional Notes

- [ ] First build takes the longest (downloading everything)
- [ ] Subsequent builds only take 1-2 minutes
- [ ] Can keep the `devel` conda environment for quick rebuilds
- [ ] Make changes to SHARPpy code, then just rebuild executable
- [ ] For major version changes, may need to `conda env remove -n devel` first

## Contact & Support

If stuck on a step:
1. Check: https://github.com/sharppy/SHARPpy/issues
2. Search build-related issues
3. Create new issue with:
   - [ ] Windows version (10/11)
   - [ ] Python version (`python --version`)
   - [ ] Full error message (copy-paste from terminal)
   - [ ] Steps to reproduce

Good luck! 🚀
