from typing import List
from collections import defaultdict
class solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for word in strs:
            key=tuple(sorted(word))
            groups[key].append(word)
        return list(groups.values())

# Read input
strs = input().split()
result = groupAnagrams(strs)
# Sort for consistent output
result = [sorted(group) for group in result]
result.sort(key=lambda x: (len(x), x[0] if x else ""))
for group in result:
    print(" ".join(group))