import re
from typing import List


def maximumValue(strs: List[str]) -> int:
    b = re.findall(r'\d+', ','.join(strs))
    a = []
    for i in strs:
        if i in b:
            a.append(int(i))
        else:
            a.append(len(i))
    a= [int(i) for i in a]
    return max(a)