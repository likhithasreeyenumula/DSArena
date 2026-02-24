import sys
def reverseNumber(n):
    sign=-1 if n<0 else 1
    n=abs(n)
    res=0
    while n>0:
        res=(res*10)+(n%10)
        n//=10
    print(res*sign)
# Read input
for line in sys.stdin:
    if line.strip():
        reverseNumber(int(line.strip()))