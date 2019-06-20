import json


class Util:
    def __init__(self, j):
        self.j = j

    def get_value_json(self):
        values = []
        data_string = json.dumps(self.j)
        decoded = json.loads(data_string)
        for value in decoded.items():
            values.append(value)
        return values