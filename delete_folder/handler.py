import os
import shutil

def handle(args):
    path = args.get("path")

    if not path:
        return {
            "status": "error",
            "message": "❌ Path missing"
        }

    if not os.path.exists(path):
        return {
            "status": "error",
            "message": f"❌ Folder does not exist:\n{path}"
        }

    try:
        shutil.rmtree(path)
        return {
            "status": "success",
            "action": "delete_folder",
            "path": path,
            "message": f"🗑️ Folder deleted successfully!\n📍 Location: {path}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Failed to delete folder\nReason: {e}"
        }
