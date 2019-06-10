import json
import os.path as path


class Configurations:
    def __init__(self):
        with open(path.join(path.dirname(__file__), 'Config.json', 'r')) as f:
            self.config = json.load(f)

    def GetConfig(self):
        return self.config
