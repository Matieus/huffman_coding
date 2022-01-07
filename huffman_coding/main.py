import yaml
from typing import Dict
from heapsort import Heapsort
from get_text_file import GetTextFile
from create_chars_dict import CreateCharsDict
from get_compresed_code import GetCompressedCode
from create_tree import CreateTree
from save_json_file import SaveJsonFile
from result_dict import ResultDict

file = GetTextFile().get_text()
print(f"text:\n{file}", '\n')

def character_count(file: str) -> Dict[str, int]:
    chars_dict: Dict[str, int]
    chars_dict = {}

    for char in file:
        if chars_dict.get(char):
            chars_dict[char] += 1

        else:
            chars_dict[char] = 1

    return chars_dict


chars_dict = character_count(file)
print(f"character count:\n{chars_dict}", "\n")

values = list(chars_dict.values())
Heapsort().heapsort(values)
print(f"values sorted by heapsort:\n{values}", '\n')


dict_tree = CreateTree(chars_dict).create_tree()
print(f"dict_tree:\n{dict_tree}", '\n')


chars_dict_code = character_count(file)
chars_dict_code = CreateCharsDict(dict_tree, chars_dict_code).create_dict()


code = GetCompressedCode().get_compressed_code(chars_dict_code)
print(f"code:\n{code}", '\n')


print("_"*30, '\n')
result_dict = ResultDict(code, dict_tree, character_count(file)).result()
SaveJsonFile(result_dict)
print(yaml.dump(result_dict, sort_keys=False, default_flow_style=False))
print("_"*30, '\n')