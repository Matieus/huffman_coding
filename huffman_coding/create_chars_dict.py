from typing import Dict

class CreateCharsDict:
    def __init__(self, tmp1: Dict[str, int], tmp2: Dict[str, int]):
        self.tmp1 = tmp1
        self.tmp2 = tmp2
        self.keys_tmp1 = list(tmp1.keys())
        self.keys_tmp2 = list(tmp2.keys())

    def create_dict(self) -> Dict[str, int]:
        i = 0
        l = str(1)
        while len(self.keys_tmp1) > 0:
            a = self.keys_tmp1.pop()
            for x in self.keys_tmp2:
                if a == x:
                    self.tmp2[x] = int(l)
            if i % 2 == 0:
                l = l + str(0)
            else:
                l = l[:-1] + str(1)
            i += 1

        return self.tmp2