import json, os


class GetDataJson:
    def __init__(self, prop):
        self.prop = prop

    def GetJson(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        with open(cwd + '/settings.json') as f:
            data = f.read()
            #    parse file
            obj = json.loads(data)
            #  print(str(obj[prop]))
            return obj[self.prop]
