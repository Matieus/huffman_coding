import json
from typing import Dict
class SaveJsonFile:
    def __init__(self, result_dict: Dict[str, int]):
        self.result_dict = result_dict
        with open("result.json", "w") as f:
            json.dump(result_dict, f, indent=4)

            

