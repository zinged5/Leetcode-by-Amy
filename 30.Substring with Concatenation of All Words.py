from typing import List
import re
from itertools import permutations
from collections import Counter
s = "foobarfoobarthefoobarman"
words = ["foo","bar"]
# s = "aaaaaaaaaaaaaa"
# words = ["aa","aa"]
# s='wordgoodgoodgoodbestword'
# words=["word","good","best","good"]
# s='barfoofoobarthefoobarman'
# words=["bar","foo","the"]

def findSubstring(s: str, words: List[str]) -> List[int]:
    perm = permutations(words)
    ans = []
    a = [s.find(''.join(words)) for i in words]
    if -1 in a:
        return []
    for i in perm:
        f = ''.join(i)
        print('count  ' ,int(s.count(f)))
        if s.find(f) >= 0:
            ans.append(s.find(f))
        if s.rfind(f) >=0:
            print(s.rfind(f))
            ans.append(s.rfind(f))
    if len(ans) >-1 :
        a = Counter(''.join(words))
        for i in a:
            if len(a.keys()) == 1 and len(''.join(words)) == a.get(i):
                d=[i for i in range(0,max(set(ans))+1)]
                print(max(set(ans)))
                return d
            else:
                return list(set(ans))
    else:
            return []

# print(findSubstring(s,words))
a=Counter(words)
print(a)

