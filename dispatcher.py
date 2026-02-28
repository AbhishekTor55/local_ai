from create_folder.handler import handle as create_folder_handler
from delete_folder.handler import handle as delete_folder_handler
from clean_python_project.handler import handle as clean_python_handler
from check_wifi_status.handler import handle as wifi_status_handler
from shutdown_system.handler import handle as shutdown_handler
from list_files.handler import handle as list_files_handler
from reboot_system.handler import handle as reboot_handler


def execute_action(data):
    intent = data.get("intent")
    args = data.get("args", {})

    # 🗂️ CREATE FOLDER
    if intent == "create_folder":
        result = create_folder_handler(args)

        if result.get("status") == "success":
            return f"📁 Folder created successfully\n📍 Location: {result.get('path')}"
        else:
            return f"❌ Failed to create folder\n⚠️ Reason: {result.get('reason')}"

    # 🗑️ DELETE FOLDER
    elif intent == "delete_folder":
        result = delete_folder_handler(args)

        if result.get("status") == "success":
            return f"🗑️ Folder deleted successfully\n📍 Location: {result.get('path')}"
        else:
            return f"❌ Failed to delete folder\n⚠️ Reason: {result.get('reason')}"

    # 🧹 CLEAN PYTHON PROJECT
    elif intent == "clean_python_project":
        result = clean_python_handler(args)

        if result.get("status") == "success":
            return (
                "🧹 Python project cleaned successfully\n"
                f"📍 Path: {result.get('path')}\n"
                f"🗑️ Removed items: {result.get('cleaned_count')}"
            )
        else:
            return f"❌ Clean failed\n⚠️ Reason: {result.get('message')}"


               # 📶 CHECK WIFI STATUS
    elif intent == "check_wifi_status":
        result = wifi_status_handler(args)

        if result.get("status") == "success":
            return result.get("message")
        else:
            return f"❌ WiFi check failed\n⚠️ {result.get('message')}" 
        
            # 🛑 SHUTDOWN SYSTEM
    elif intent == "shutdown_system":
        result = shutdown_handler(args)
        return result.get("message")
    
        # 📂 LIST FILES
    elif intent == "list_files":
        result = list_files_handler(args)
        return result.get("message")
    
        # 🔄 REBOOT SYSTEM
    elif intent == "reboot_system":
        result = reboot_handler(args)
        return result.get("message")
        

    # ❌ UNSUPPORTED COMMAND
    return "❌ Command not supported"
