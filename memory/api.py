from memory.memory import MemoryEngine

memory = MemoryEngine()


# -------------------------
# GENERIC SET / GET
# -------------------------

def set_value(key, value):

    if key == "user_name":
        memory.set_user_name(value)


def get_value(key):

    if key == "user_name":
        return memory.get_user_name()

    return None


# -------------------------
# COMMAND MEMORY
# -------------------------

def add_command(command):

    memory.add_command(command)


def get_commands():

    return memory.get_last_commands()


# -------------------------
# ERROR MEMORY
# -------------------------

def add_error(error):

    memory.add_error(error)


def get_errors():

    return memory.get_errors()


# -------------------------
# MISTAKE MEMORY
# -------------------------

def add_mistake(mistake):

    memory.add_mistake(mistake)


def get_mistakes():

    return memory.get_mistakes()