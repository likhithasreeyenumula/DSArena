def factorialIterative(n: int) -> int:
    result = 1
    for i in range(1,n+1):
        result*=i
    return result
def factorialRecursive(n: int) -> int:
    if n==0 or n==1:
        return 1
    return n * factorialRecursive(n-1)
# Read input
n = int(input())
print(factorialIterative(n),
factorialRecursive(n))