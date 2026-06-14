# 🚀 Quick Start: Build SHARPpy Windows Executable

## The Simple Way (3 Steps)

### 1️⃣ Install Anaconda
- Download from: https://www.anaconda.com/products/individual
- Run the installer
- Restart your computer

### 2️⃣ Open Anaconda Prompt
- Search for "Anaconda Prompt" in Windows Start menu
- Right-click → "Run as Administrator"

### 3️⃣ Build It!
```cmd
cd C:\path\to\SHARPpy
build_windows_exe.bat
```

**That's it!** ✓

The script will:
- ✓ Create a Python environment
- ✓ Install all dependencies
- ✓ Build the executable
- ✓ Show success message

Takes 5-15 minutes on first build.

---

## Where's My Executable?

After the script finishes, your executable is in:
```
C:\path\to\SHARPpy\dist\SHARPpy.exe
```

or

```
C:\path\to\SHARPpy\dist\SHARPpy\SHARPpy.exe
```

Just **double-click to run!** 🎉

---

## Need Help?

### Before You Start
Run this to verify your system is ready:
```cmd
python check_build_ready.py
```

### Full Documentation
- **Comprehensive Guide**: `BUILD_WINDOWS_EXECUTABLE.md`
- **Step-by-Step Checklist**: `BUILD_CHECKLIST.md`
- **Quick Reference**: `WINDOWS_BUILD_GUIDE.md`
- **Troubleshooting**: See BUILD_WINDOWS_EXECUTABLE.md for detailed solutions

### Quick Troubleshooting

**"Anaconda not found?"**
```cmd
:: Make sure you're using Anaconda Prompt, not regular Command Prompt
```

**"Build failed?"**
```cmd
:: Try removing the environment and rebuilding:
conda env remove -n devel
build_windows_exe.bat
```

**"Executable won't start?"**
```cmd
:: First run takes 10-30 seconds, try again
:: Check you have at least 2GB disk space
```

---

## Advanced Options

### PowerShell Version
```powershell
.\build_windows_exe.ps1
```

### Single File Executable
```cmd
cd runsharp
pyinstaller SHARPpy-win.spec --onefile
```

### Creating an Installer
See: `BUILD_WINDOWS_EXECUTABLE.md` (section: Creating an Installer)

---

## What You Get

- **Standalone executable** - No Python installation needed
- **Portable** - Works on Windows 7 SP1 and later
- **Shareable** - Can give to anyone with Windows
- **Full featured** - Same as Python version
- **Sized**: ~200-400 MB

---

## More Info

- **GitHub**: https://github.com/sharppy/SHARPpy
- **Documentation**: http://sharppy.github.io/SHARPpy/
- **Issues**: https://github.com/sharppy/SHARPpy/issues

---

**Ready?** Open Anaconda Prompt and run:
```cmd
build_windows_exe.bat
```

Good luck! 🌩️🎯
