def swap(a: int, b: int) -> str:
    return b,a

# Read input
a, b = map(int, input().split())
a,b=swap(a,b)
print(a,b)