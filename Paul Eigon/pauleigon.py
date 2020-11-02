n,a,b=input().split()
n=int(n)
a=int(a)
b=int(b)
c=a+b
d=c//n
if d%2==0:
    print("paul")
else:
    print("opponent")
