import yaml
from get_json_data import GetJsonData
from heapsort import Heapsort
from get_text_file import GetTextFile
from create_chars_dict import CreateCharsDict
from get_compresed_code import GetCompressedCode
from character_count import CharacterCount
from create_tree import CreateTree
from save_json_file import SaveJsonFile
from result_dict import ResultDict


file = GetTextFile().get_text()
print(f"text:\n{file}", '\n')


chars_dict = CharacterCount().character_count(file)
print(f"character count:\n{chars_dict}", "\n")

values = list(chars_dict.values())
Heapsort().heapsort(values)
print(f"values sorted by heapsort:\n{values}", '\n')


dict_tree = CreateTree(chars_dict).create_tree()
print(f"dict_tree:\n{dict_tree}", '\n')


dict_code = CharacterCount().character_count(file)
dict_code = CreateCharsDict(dict_tree, dict_code).create_dict()
print(f"chars_dict_code:\n{dict_code}", '\n')

code = GetCompressedCode().get_compressed_code(dict_code)
print(f"code:\n{code}", '\n')


print("_"*30, '\n')
result_dict = ResultDict(code, dict_tree, 
    CharacterCount().character_count(file), dict_code).result()

SaveJsonFile(result_dict)
print(yaml.dump(result_dict, sort_keys=False, default_flow_style=False))
print("_"*30, '\n')


'''
result_dict = GetJsonData().get_dict()
print(yaml.dump(result_dict, sort_keys=False, default_flow_style=False))
'''