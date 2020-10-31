n=int(input())
res=0
while n:
    res=(res<<1)|(n&1)
    n>>=1
print(res)
