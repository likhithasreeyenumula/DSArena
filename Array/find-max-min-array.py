from typing import List

def findMaxMin(nums: List[int]) -> str:
    mn=nums[0]
    mx=nums[0]
    for i in nums:
        if i < mn:
            mn=i
        if i > mx:
            mx=i
    return f"{mn} {mx}"

# Read input
nums = list(map(int, input().split()))
print(findMaxMin(nums))