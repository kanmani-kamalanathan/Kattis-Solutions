import math
n,a,b=input().split()
n=int(n)
a=int(a)
b=int(b)
c=math.sqrt((a**2)+(b**2))
x=[]
for i in range(0,n):
    x.append(int(input()))
for i in x:
    if ((i<=a)or(i<=b)or(i<=c)):
        print('DA')
    else:
        print('NE')
