from typing import List
def twoSum(nums:List[int],target:int) -> List[int]:
    seen = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in seen:
            return[seen[rem],i]
        seen[nums[i]] = i
        
    return []

# Read input
nums=list(map(int,input().split()))
target=int(input())
print(" ".join(map(str,twoSum(nums,target))))