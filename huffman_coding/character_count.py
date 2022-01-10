from typing import Dict

class CharacterCount():
    def character_count(self, file: str) -> Dict[str, int]:
        chars_dict: Dict[str, int]
        chars_dict = {}

        for char in file:
            if chars_dict.get(char):
                chars_dict[char] += 1

            else:
                chars_dict[char] = 1

        return chars_dict