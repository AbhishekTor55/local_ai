from memory.session import SessionMemory

session = SessionMemory()


def get_last_command():

    return session.get_command()


def get_context():

    last = session.get_command()

    if not last:
        return None

    return f"Last command was {last}"