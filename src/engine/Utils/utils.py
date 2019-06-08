import json
class util:
    def get_value_json(j):
        values = []
        data_string = json.dumps(j)
        decoded = json.loads(data_string)
        for key,value in decoded.items():
           values.append(value)
        return values