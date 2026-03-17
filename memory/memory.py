import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "memory.json")


class MemoryEngine:

    def __init__(self):
        self.memory = self.load_memory()

    def load_memory(self):

        if not os.path.exists(MEMORY_FILE):

            return {
                "user": {"name": ""},
                "last_commands": [],
                "errors": [],
                "common_mistakes": []
            }

        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def save_memory(self):

        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=4)

    # USER NAME STORAGE

    def set_user_name(self, name):

        self.memory["user"]["name"] = name
        self.save_memory()

    def get_user_name(self):

        return self.memory["user"]["name"]

    # COMMAND HISTORY

    def add_command(self, command):

        self.memory["last_commands"].append(command)

        self.memory["last_commands"] = self.memory["last_commands"][-20:]

        self.save_memory()

    def get_last_commands(self):

        return self.memory["last_commands"]

    # ERROR TRACKING

    def add_error(self, error):

        self.memory["errors"].append(error)

        self.memory["errors"] = self.memory["errors"][-20:]

        self.save_memory()

    def get_errors(self):

        return self.memory["errors"]

    # COMMON MISTAKES

    def add_mistake(self, mistake):

        self.memory["common_mistakes"].append(mistake)

        self.save_memory()

    def get_mistakes(self):

        return self.memory["common_mistakes"]