import json

class SaveJsonFile:
    def __init__(self, result_dict):
        self.result_dict = result_dict
        with open("result.json", "w") as f:
            json.dump(result_dict, f, indent=4)

            

