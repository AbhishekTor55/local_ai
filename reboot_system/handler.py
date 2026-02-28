import subprocess


def handle(args=None):
    try:
        # safer than raw reboot
        subprocess.Popen(
            ["shutdown", "-r", "now"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return {
            "status": "success",
            "message": "🔄 System reboot initiated..."
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Reboot failed: {str(e)}"
        }