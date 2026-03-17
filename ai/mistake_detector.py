from memory.memory import MemoryEngine

memory = MemoryEngine()


def detect_previous_error():

    errors = memory.get_errors()

    if not errors:
        return None

    last_error = errors[-1]

    return f"⚠️ Last error: {last_error}"