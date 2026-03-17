from memory.memory import MemoryEngine

memory = MemoryEngine()


def learn_user_habit():

    commands = memory.get_last_commands()

    if not commands:
        return None

    if commands.count("nano") > 3:
        return "💡 You often use nano. Try VSCode editor?"

    return None