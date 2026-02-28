import subprocess


def handle(args=None):
    try:
        # nmcli is standard on most Linux systems
        result = subprocess.check_output(
            ["nmcli", "-t", "-f", "ACTIVE,SSID", "dev", "wifi"],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        for line in result.splitlines():
            if line.startswith("yes:"):
                ssid = line.split("yes:")[1]
                return {
                    "status": "success",
                    "connected": True,
                    "ssid": ssid,
                    "message": f"📶 WiFi connected\n📡 Network: {ssid}"
                }

        return {
            "status": "success",
            "connected": False,
            "message": "❌ WiFi disconnected"
        }

    except FileNotFoundError:
        return {
            "status": "error",
            "message": "❌ nmcli not found (NetworkManager missing)"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"❌ Failed to check WiFi status: {str(e)}"
        }