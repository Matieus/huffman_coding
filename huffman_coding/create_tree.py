from heapsort import Heapsort
from typing import Dict
from get_key import GetKey

class CreateTree:
    def __init__(self, chars_dict: Dict[str, int]):
        self.chars_dict = chars_dict


    def create_tree(self) -> Dict[str, int]:
        dict_tree: Dict[str, int]
        dict_tree = {}

        values = list(self.chars_dict.values())
        Heapsort().heapsort(values)
        
        while (len(values) >= 2):
            i = values.pop(0)
            a = GetKey(self.chars_dict).get_key(i)
            self.chars_dict.pop(a)

            Heapsort().heapsort(values)

            j = values.pop(0)
            b = GetKey(self.chars_dict).get_key(j)
            self.chars_dict.pop(b)
            c = str(a) + str(b)
            z = j + i
            self.chars_dict[c] = z

            dict_tree[a] = i
            dict_tree[b] = j
            dict_tree[c] = z

            values.append(z)
            Heapsort().heapsort(values)

        return dict_tree