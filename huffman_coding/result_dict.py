from typing import Dict
import ast

class ResultDict():

    def __init__(self, result: str, dict_tree: Dict[str, int], chars_dict: Dict[str, int]):
        self.code, self.dict_code = result.split("\n")       
        self.dict_tree = dict_tree
        self.chars_dict = chars_dict


    def result(self):
        result_dict = {}
        result_dict["code"] = self.code
        result_dict["dict_code"] = ast.literal_eval(self.dict_code)
        result_dict["dict_tree"] = self.dict_tree
        result_dict["chars_dict"] = self.chars_dict

        return result_dict