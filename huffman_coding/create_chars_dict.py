from typing import Dict

class CreateCharsDict:
    def __init__(self, dict_tree: Dict[str, int], dict_code: Dict[str, int]):
        self.dict_tree = dict_tree
        self.dict_code = dict_code
        self.keys_dict_tree = list(dict_tree.keys())
        self.keys_dict_code = list(dict_code.keys())

    def create_dict(self) -> Dict[str, int]:
        i = 0
        left = str(1)
        
        while len(self.keys_dict_tree) > 0:
            a = self.keys_dict_tree.pop()
            for x in self.keys_dict_code:
                if a == x:
                    self.dict_code[x] = int(left)
            if i % 2 == 0:
                left = left + str(0)
            else:
                left = left[:-1] + str(1)
            i += 1

        return self.dict_code