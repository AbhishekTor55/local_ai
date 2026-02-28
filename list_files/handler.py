import os


def handle(args):
    path = args.get("path")

    # ✅ Default path if missing
    if not path:
        path = os.path.expanduser("~")

    # ✅ Convert relative to absolute
    path = os.path.abspath(os.path.expanduser(path))

    if not os.path.exists(path):
        return {
            "status": "error",
            "message": f"❌ Path does not exist:\n{path}"
        }

    if not os.path.isdir(path):
        return {
            "status": "error",
            "message": f"❌ Not a directory:\n{path}"
        }

    try:
        items = os.listdir(path)

        if not items:
            return {
                "status": "success",
                "message": f"📂 Directory is empty:\n{path}"
            }

        formatted = "\n".join(f"• {item}" for item in items)

        return {
            "status": "success",
            "message": f"📂 Files in:\n{path}\n\n{formatted}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Failed to list files:\n{str(e)}"
        }