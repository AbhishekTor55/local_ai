from memory.api import get_errors, get_commands


def check_previous_errors(intent):

    errors = get_errors()

    if not errors:
        return None

    last_error = errors[-1]

    if intent in last_error:
        return f"⚠️ Last time this command failed:\n{last_error}"

    return None


def check_command_history(intent):

    commands = get_commands()

    if intent in commands:
        return f"ℹ️ You used '{intent}' command before."

    return None