def charFrequency(s: str) -> str:
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    result=[]
    for ch in sorted (freq):
        result.append(f"{ch}:{freq[ch]}")
    return " ".join(result)

# Read input
s = input()
print(charFrequency(s))