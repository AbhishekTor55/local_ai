class SessionMemory:

    def __init__(self):
        self.session = {
            "current_task": None,
            "current_command": None,
            "current_directory": None
        }

    # --------------------
    # CURRENT TASK
    # --------------------

    def set_task(self, task):
        self.session["current_task"] = task

    def get_task(self):
        return self.session["current_task"]

    # --------------------
    # CURRENT COMMAND
    # --------------------

    def set_command(self, command):
        self.session["current_command"] = command

    def get_command(self):
        return self.session["current_command"]

    # --------------------
    # CURRENT DIRECTORY
    # --------------------

    def set_directory(self, path):
        self.session["current_directory"] = path

    def get_directory(self):
        return self.session["current_directory"]