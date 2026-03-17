from memory.memory import MemoryEngine

memory = MemoryEngine()


def predict_mistake(intent):

    mistakes = memory.get_mistakes()

    if not mistakes:
        return None

    if "dependency" in str(mistakes):
        return "⚠️ Dependency missing ho sakti hai. Install karna hai?"

    if "wrong path" in str(mistakes):
        return "⚠️ Path check karo."

    return None