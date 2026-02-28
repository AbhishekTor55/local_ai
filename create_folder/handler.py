import os

def handle(args):
    path = args.get("path")

    if not path:
        return {
            "status": "error",
            "action": "create_folder",
            "message": "❌ Path missing. Folder create nahi ho paaya."
        }

    try:
        os.makedirs(path, exist_ok=True)

        return {
            "status": "success",
            "action": "create_folder",
            "path": path,
            "message": f"📁 Folder created successfully!\n📍 Location: {path}"
        }

    except Exception as e:
        return {
            "status": "error",
            "action": "create_folder",
            "message": f"❌ Failed to create folder.\nReason: {e}"
        }


