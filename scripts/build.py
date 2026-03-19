from pathlib import Path
from shutil import copy2, copytree, make_archive, rmtree

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PACKAGE_DIR = DIST / "python-app"

if DIST.exists():
    rmtree(DIST)

PACKAGE_DIR.mkdir(parents=True)
copy2(ROOT / "app.py", PACKAGE_DIR / "app.py")
copytree(ROOT / "templates", PACKAGE_DIR / "templates")
copy2(ROOT / "Dockerfile", PACKAGE_DIR / "Dockerfile")
copy2(ROOT / "docker-compose.yml", PACKAGE_DIR / "docker-compose.yml")

archive_base = DIST / "python-app"
make_archive(str(archive_base), "zip", root_dir=PACKAGE_DIR)
print("Build complete. Deployment bundle created in dist/.")
