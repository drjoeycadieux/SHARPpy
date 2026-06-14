# -*- mode: python -*-
"""
Improved PyInstaller spec file for building SHARPpy Windows executable
This version has better error handling and cross-platform path support
"""
import sys
import glob
import sharppy
from sharppy._version import get_versions
import os

WIN_PATH = os.getcwd()

print("PATH TO SHARPPY:", sharppy.__file__)
print("BUILD PATH:", WIN_PATH)

# Write the versions file using versioneer, because PyInstaller doesn't do this automatically
try:
    ver = get_versions()
    ver = str(ver)
    ver_fname = os.path.join(os.path.dirname(sharppy.__file__), "_version.py")
    with open(ver_fname, 'w') as ver_file:
        ver_file.write("def get_versions():\n")
        ver_file.write('    return ' + ver)
    print(f"Version file written to: {ver_fname}")
except Exception as e:
    print(f"Warning: Could not update version file: {e}")

# Re-import to get updated version
del sharppy
import sharppy

# Define paths using os.path.join for cross-platform compatibility
sharppy_dir = os.path.dirname(sharppy.__file__)
databases_dir = os.path.join(sharppy_dir, "databases")
sars_dir = os.path.join(databases_dir, "sars")
shapefiles_dir = os.path.join(databases_dir, "shapefiles")
datasources_dir = os.path.join(os.path.dirname(WIN_PATH), "datasources")
rc_dir = os.path.join(os.path.dirname(WIN_PATH), "rc")

print(f"Databases dir: {databases_dir}")
print(f"Datasources dir: {datasources_dir}")
print(f"RC dir: {rc_dir}")

# Analysis configuration
a = Analysis(
    ['SHARPpy.py'],
    pathex=[os.path.join(WIN_PATH, 'runsharp'), WIN_PATH],
    binaries=[],
    datas=[],
    hiddenimports=[
        'xml.etree.ElementTree',
        'sharppy.io.pecan_decoder',
        'sharppy.io.spc_decoder',
        'sharppy.io.buf_decoder',
        'sharppy.io.uwyo_decoder',
        'sharppy.io.nucaps_decoder',
        'datasources.available',
        'sharppy.sharptab.prof_collection',
        'certifi',
        'pkg_resources.py2_warn'
    ],
    hookspath=None,
    runtime_hooks=None,
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None
)

print("\nCleaning up binaries...")
# Remove empty binaries
a.binaries = [(name, path, typ) for name, path, typ in a.binaries if name]

print("Adding data files...")
# Add database files
db_files = [
    ("PW-mean-inches.txt", "sharppy/databases/"),
    ("PW-stdev-inches.txt", "sharppy/databases/"),
    ("sars_hail.txt", "sharppy/databases/"),
    ("sars_supercell.txt", "sharppy/databases/"),
]

for fname, dest in db_files:
    src_path = os.path.join(databases_dir, fname)
    if os.path.exists(src_path):
        a.datas.append((dest + fname, src_path, "DATA"))
        print(f"  Added: {fname}")
    else:
        print(f"  Warning: Not found: {src_path}")

# Add SARS data
print("Adding SARS data...")
sars_hail_dir = os.path.join(sars_dir, "hail")
sars_supr_dir = os.path.join(sars_dir, "supercell")

if os.path.exists(sars_hail_dir):
    for hail_file in glob.glob(os.path.join(sars_hail_dir, "*")):
        if os.path.isfile(hail_file):
            a.datas.append((
                os.path.join("sharppy/databases/sars/hail/", os.path.basename(hail_file)),
                hail_file,
                "DATA"
            ))

if os.path.exists(sars_supr_dir):
    for supr_file in glob.glob(os.path.join(sars_supr_dir, "*")):
        if os.path.isfile(supr_file):
            a.datas.append((
                os.path.join("sharppy/databases/sars/supercell/", os.path.basename(supr_file)),
                supr_file,
                "DATA"
            ))

# Add shapefiles
print("Adding shapefiles...")
if os.path.exists(shapefiles_dir):
    for shapefile in glob.glob(os.path.join(shapefiles_dir, "*")):
        if os.path.isfile(shapefile):
            a.datas.append((
                os.path.join("sharppy/databases/shapefiles/", os.path.basename(shapefile)),
                shapefile,
                "DATA"
            ))

# Add RC files (icons, images, etc.)
print("Adding resource files...")
if os.path.exists(rc_dir):
    for rc_file in glob.glob(os.path.join(rc_dir, "*.png")):
        a.datas.append((
            os.path.join("rc/", os.path.basename(rc_file)),
            rc_file,
            "DATA"
        ))

# Add datasource files
print("Adding datasource files...")
if os.path.exists(datasources_dir):
    for ds_file in glob.glob(os.path.join(datasources_dir, "*")):
        if os.path.isfile(ds_file) and "__pycache__" not in ds_file:
            a.datas.append((
                os.path.join("sharppy/datasources/", os.path.basename(ds_file)),
                ds_file,
                "DATA"
            ))

# Remove Python config files if present
a.datas = [(d, s, t) for d, s, t in a.datas if 'pyconfig' not in d]

print(f"\nTotal data files added: {len(a.datas)}")

# Build PYZ
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Build EXE
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='SHARPpy',
    debug=False,
    strip=False,
    upx=True,
    console=False,  # Set to True if you want a console window
    icon=os.path.join(os.path.dirname(__file__), 'icons', 'SHARPpy.ico') if os.path.exists(os.path.join(os.path.dirname(__file__), 'icons', 'SHARPpy.ico')) else None
)

print("\nBuild configuration complete!")
print("="*60)
print(f"Output executable: SHARPpy.exe")
print(f"Output directory: dist/SHARPpy/")
print("="*60)

# Attempt to revert the _version.py file to original using git
try:
    import subprocess
    ver_fname = os.path.join(os.path.dirname(sharppy.__file__), "_version.py")
    subprocess.run(['git', 'checkout', '--', ver_fname], check=False, capture_output=True)
except Exception as e:
    print(f"Note: Could not revert _version.py file with git: {e}")
