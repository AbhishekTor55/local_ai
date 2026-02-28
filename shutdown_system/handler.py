import subprocess


def handle(args=None):
    try:
        # Linux system shutdown command
        subprocess.Popen(
            ["shutdown", "-h", "now"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return {
            "status": "success",
            "message": "🛑 System shutdown initiated..."
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Shutdown failed: {str(e)}"
        }