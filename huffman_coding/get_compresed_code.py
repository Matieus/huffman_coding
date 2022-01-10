from get_text_file import GetTextFile
from typing import Dict

class GetCompressedCode():
    def __init__(self):
        self.file = GetTextFile().get_text()

    def get_compressed_code(self, chars_dict_code: Dict[str, int]) -> str:
        code = ""
        for x in self.file:
            for i in x:
                for n in chars_dict_code:
                    if n == i:
                        code = code + str(chars_dict_code[n])

        code = f"{code}"
        return code