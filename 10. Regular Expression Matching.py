import re
s='aa'
p='a*'

def isMatch(s: str, p: str) -> bool:
    result = re.fullmatch(p, s)
    return result !=None

print(isMatch(s,p))


