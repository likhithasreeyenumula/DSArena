s=input().strip()
if not s:
    print(s)
else:
    res=[]
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count +=1
        else:
            res.append(s[i-1]+str(count))
            count=1
    res.append(s[-1]+str(count))
    compressed="".join(res)
    if (len(compressed)<len(s)):
        print(compressed)
    else:
        print(s)