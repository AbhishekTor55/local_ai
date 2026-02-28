import os
import shutil

CLEAN_TARGETS = [
    "__pycache__",
    ".pytest_cache",
    "build",
    "dist"
]

FILE_EXTENSIONS = [".pyc", ".pyo"]

def handle(args):
    base_path = args.get("path", "/home/user")

    if not os.path.exists(base_path):
        return {
            "status": "error",
            "message": f"Path does not exist: {base_path}"
        }

    removed = []

    for root, dirs, files in os.walk(base_path):
        # remove directories
        for d in dirs:
            if d in CLEAN_TARGETS or d.endswith(".egg-info"):
                full_path = os.path.join(root, d)
                try:
                    shutil.rmtree(full_path)
                    removed.append(full_path)
                except Exception:
                    pass

        # remove files
        for f in files:
            if any(f.endswith(ext) for ext in FILE_EXTENSIONS):
                full_path = os.path.join(root, f)
                try:
                    os.remove(full_path)
                    removed.append(full_path)
                except Exception:
                    pass

    return {
        "status": "success",
        "action": "clean_python_project",
        "cleaned_count": len(removed),
        "path": base_path
    }
