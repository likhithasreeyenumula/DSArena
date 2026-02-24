from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    freq={}
    duplicates=[]
    for i in nums:
        freq[i]=freq.get(i,0)+1
    for i in freq:
        if freq[i]>1:
            duplicates.append(i)
    return duplicates

# Read input
nums = list(map(int, input().split()))
result = findDuplicates(nums)
print(' '.join(map(str, result)) if result else 'None')