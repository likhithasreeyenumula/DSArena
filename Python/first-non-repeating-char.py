def firstNonRepeating(s: str) -> str:
    freq={}
    for ch in s:
        freq [ch]=freq.get(ch,0)+1
    for ch in s:
        if freq[ch]==1:
            return ch
    return -1
    pass

# Read input
s = input()
print(firstNonRepeating(s))