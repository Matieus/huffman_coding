from typing import Dict

class ResultDict():

    def __init__(self, code: str, dict_tree: Dict[str, int], chars_dict: Dict[str, int], dict_code: Dict[str, int]):
        self.code = code
        self.dict_code = dict_code    
        self.dict_tree = dict_tree
        self.chars_dict = chars_dict

    def result(self) -> Dict[str, int]:
        result_dict = {}
        result_dict["code"] = self.code
        result_dict["dict_tree"] = self.dict_tree
        result_dict["chars_dict"] = self.chars_dict
        result_dict["dict_code"] = self.dict_code

        return result_dict