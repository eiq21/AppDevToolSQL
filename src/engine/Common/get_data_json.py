import json,os

class get_config:
    def get_json(prop):
     cwd = os.path.dirname(os.path.realpath(__file__))
     with open(cwd + '/settings.json') as f:
           data = f.read()
        #    parse file
           obj = json.loads(data)
            #  print(str(obj[prop]))
           return obj[prop]
         

