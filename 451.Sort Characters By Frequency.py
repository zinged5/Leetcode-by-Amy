from collections import Counter
# word2='Aabb'
word2='tree'

def frequencySort( s: str) -> str:
    word = Counter(s)
    new_word=[]
    b=[[word.get(i),i] for i in word]
    print(sorted(b , reverse=True))
    for i,v in sorted(b , reverse=True):
        new_word.append(v*i)
    return ''.join(new_word)