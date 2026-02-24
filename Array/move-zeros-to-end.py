from typing import List

def moveZeros(nums: List[int]) -> List[int]:
    i=0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i],nums[j]=nums[j],nums[i]
            i += 1
    return nums

# Read input
nums = list(map(int, input().split()))
result = moveZeros(nums)
print(' '.join(map(str, result)))