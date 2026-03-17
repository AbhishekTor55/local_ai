def parse_intent(text):

    text = text.lower()

    if "create folder" in text:
        name = text.split("create folder")[-1].strip()

        return {
            "intent": "create_folder",
            "args": {"name": name}
        }

    if "delete folder" in text:
        name = text.split("delete folder")[-1].strip()

        return {
            "intent": "delete_folder",
            "args": {"name": name}
        }

    if "list files" in text:
        return {
            "intent": "list_files",
            "args": {}
        }

    if "wifi status" in text:
        return {
            "intent": "check_wifi_status",
            "args": {}
        }

    if "shutdown system" in text:
        return {
            "intent": "shutdown_system",
            "args": {}
        }

    if "reboot system" in text:
        return {
            "intent": "reboot_system",
            "args": {}
        }

    return {
        "intent": "unknown",
        "args": {}
    }