import json

class JsonHandler:
    def __init__(self, json_file):

        with open(json_file) as json_data:
            self.json_data = json.load(json_data)

        self.keys = list(dict(self.json_data).keys())