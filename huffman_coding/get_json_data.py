import json

class GetJsonData():
    def __init__(self):
        with open("result.json", "r") as f:
            self.result_dict = json.load(f)

    def get_dict(self):
        return self.result_dict