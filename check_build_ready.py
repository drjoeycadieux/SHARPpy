#!/usr/bin/env python
"""
Quick Setup Helper for SHARPpy Windows Build
This script helps verify that your system is ready to build the Windows executable
"""

import os
import sys
import platform
import subprocess

def check_anaconda():
    """Check if Anaconda/Miniconda is installed"""
    try:
        result = subprocess.run(['conda', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout.strip()
    except:
        pass
    return False, "Not found"

def check_python():
    """Check Python version"""
    return sys.version

def check_disk_space():
    """Check available disk space"""
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        free_gb = free / (1024**3)
        return free_gb >= 3, f"{free_gb:.2f} GB"
    except:
        return None, "Unknown"

def check_files():
    """Check if required files exist"""
    required_files = {
        'environment.yml': 'Conda environment file',
        'setup.py': 'Setup configuration',
        'build_windows_exe.bat': 'Windows build script',
        'runsharp/SHARPpy-win.spec': 'PyInstaller spec file',
    }
    
    results = {}
    for filename, description in required_files.items():
        exists = os.path.exists(filename)
        results[filename] = (exists, description)
    return results

def main():
    print("\n" + "="*60)
    print("SHARPpy Windows Build - Pre-Flight Check")
    print("="*60 + "\n")
    
    # Check OS
    print(f"Operating System: {platform.system()} {platform.release()}")
    if platform.system() != "Windows":
        print("  ⚠ Warning: This is for Windows only!")
        print("  On Linux/macOS, use: python setup.py install")
    else:
        print("  ✓ Windows detected")
    
    print()
    
    # Check Anaconda
    print("Checking Anaconda/Miniconda...")
    conda_ok, conda_version = check_anaconda()
    if conda_ok:
        print(f"  ✓ Found: {conda_version}")
    else:
        print(f"  ✗ Not found!")
        print("  → Download from: https://www.anaconda.com/products/individual")
    
    print()
    
    # Check Python
    print(f"Python Version: {sys.version.split()[0]}")
    
    print()
    
    # Check Disk Space
    print("Checking disk space...")
    disk_ok, disk_info = check_disk_space()
    if disk_ok:
        print(f"  ✓ {disk_info} available (need ~3GB)")
    elif disk_ok is None:
        print(f"  ? {disk_info}")
    else:
        print(f"  ✗ {disk_info} available (need at least 3GB)")
    
    print()
    
    # Check Files
    print("Checking required files...")
    files = check_files()
    all_ok = True
    for filename, (exists, description) in files.items():
        status = "✓" if exists else "✗"
        print(f"  {status} {filename}: {description}")
        if not exists:
            all_ok = False
    
    print()
    print("="*60)
    
    if conda_ok and all_ok:
        print("✓ ALL CHECKS PASSED!")
        print("\nYou're ready to build! Run:")
        print("  build_windows_exe.bat")
        print("\nOr if using PowerShell:")
        print("  .\\build_windows_exe.ps1")
    else:
        print("⚠ SOME CHECKS FAILED")
        if not conda_ok:
            print("\n• Anaconda/Miniconda is required:")
            print("  1. Download from https://www.anaconda.com/products/individual")
            print("  2. Run the installer")
            print("  3. Restart your terminal")
        if not all_ok:
            print("\n• Missing required files:")
            print("  Make sure you're in the SHARPpy root directory")
    
    print("\n" + "="*60)
    print("\nFor detailed instructions, see:")
    print("  • BUILD_WINDOWS_EXECUTABLE.md (comprehensive guide)")
    print("  • WINDOWS_BUILD_GUIDE.md (quick reference)")
    print("  • BUILD_CHECKLIST.md (step-by-step checklist)")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
