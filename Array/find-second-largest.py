from typing import List

def secondLargest(nums: List[int]) -> int:
    if len(nums) < 2:
        return -1
    largest=-10**18
    second=-10**18
    for i in nums: 
        if i >largest:
            second=largest
            largest=i
        elif i != largest and i >second:
            second=i
    if second==-10**18:
        return -1
    return second

# Read input
nums = list(map(int, input().split()))
print(secondLargest(nums))