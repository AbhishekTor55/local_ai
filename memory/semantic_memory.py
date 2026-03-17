from memory.memory import MemoryEngine

memory = MemoryEngine()


def save_semantic_note(note):

    errors = memory.get_errors()

    errors.append(note)

    memory.memory["errors"] = errors

    memory.save_memory()


def get_last_semantic_note():

    errors = memory.get_errors()

    if not errors:
        return None

    return errors[-1]