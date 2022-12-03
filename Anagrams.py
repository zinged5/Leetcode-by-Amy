import itertools
from collections import defaultdict
from dataclasses import dataclass
from typing import List

@dataclass
class Anagram:


    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = False
        if sorted(list(s)) == sorted(list(t)):
            is_anagram = True
        return is_anagram

strs=["eat","tea","tan","ate","nat","bat"]
temp = defaultdict(list)

for ele in strs:
    temp[str(sorted(ele))].append(ele)
    print(str(sorted(ele)))
res = list(temp.keys())
# sorted(indexes)

print( str(res))





if __name__ == '__main__':
    print("")
    # str=["eat","tea","tan","ate","nat","bat"]
    # anagram = Anagram()
    # anagram.groupAnagrams(str)