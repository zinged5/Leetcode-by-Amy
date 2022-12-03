from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        elif len(word1) == len(word2):
            a = Counter(word1)
            b = Counter(word2)
            if set(word1) == set(word2) and sorted(a.values()) == sorted(b.values()):
                return  True
            else:
                return False