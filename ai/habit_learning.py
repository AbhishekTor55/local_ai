from memory.memory import MemoryEngine

memory = MemoryEngine()


def analyze_user_habits():

    commands = memory.get_last_commands()

    if not commands:
        return None

    most_used = max(set(commands), key=commands.count)

    if commands.count(most_used) > 3:
        return f"💡 You often use '{most_used}' command."

    return None