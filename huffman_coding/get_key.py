from typing import Dict

class GetKey:
    def __init__(self, chars_dict: Dict[str, int]):
        self.chars_dict = chars_dict

    def get_key(self, val: int) -> str:
        for key, value in self.chars_dict.items():
            if val == value:
                return key