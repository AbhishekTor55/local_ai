from create_folder.handler import handle as create_folder_handler
from delete_folder.handler import handle as delete_folder_handler
from clean_python_project.handler import handle as clean_python_handler
from check_wifi_status.handler import handle as wifi_status_handler
from shutdown_system.handler import handle as shutdown_handler
from list_files.handler import handle as list_files_handler
from reboot_system.handler import handle as reboot_handler
from memory.session_memory import SessionMemory
from memory.memory import MemoryEngine
from ai.memory_helper import check_previous_errors


memory = MemoryEngine()
session = SessionMemory()

def execute_action(data):
    intent = data.get("intent")
    args = data.get("args", {})

    # 🧠 MEMORY CHECK
    warning = check_previous_errors(intent)
    if warning:
        print(warning)

    # 🧠 MEMORY SAVE
    memory.add_command(intent)

    # 🧠 SESSION MEMORY
    session.set_command(intent)

    # 🗂️ CREATE FOLDER
    if intent == "create_folder":
        result = create_folder_handler(args)

        if result.get("status") == "success":
            return f"📁 Folder created successfully\n📍 Location: {result.get('path')}"
        else:
            reason = result.get("reason")
            memory.add_error(f"create_folder: {reason}")

            if "exist" in str(reason).lower():
                memory.add_mistake("folder already exists")

            return f"❌ Failed to create folder\n⚠️ Reason: {reason}"

    # 🗑️ DELETE FOLDER
    elif intent == "delete_folder":
        result = delete_folder_handler(args)

        if result.get("status") == "success":
            return f"🗑️ Folder deleted successfully\n📍 Location: {result.get('path')}"
        else:
            reason = result.get("reason")
            memory.add_error(f"delete_folder: {reason}")
            return f"❌ Failed to delete folder\n⚠️ Reason: {reason}"

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
            reason = result.get("message")
            memory.add_error(f"clean_python_project: {reason}")
            return f"❌ Clean failed\n⚠️ Reason: {reason}"

    # 📶 CHECK WIFI STATUS
    elif intent == "check_wifi_status":
        result = wifi_status_handler(args)

        if result.get("status") == "success":
            return result.get("message")
        else:
            reason = result.get("message")
            memory.add_error(f"check_wifi_status: {reason}")
            return f"❌ WiFi check failed\n⚠️ {reason}"

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