# s = "   fly me   to   the moon  "

def lengthOfLastWord(self, s: str) -> int:
    return len(s.strip().split()[-1])

# print(lengthOfLastWord(s))