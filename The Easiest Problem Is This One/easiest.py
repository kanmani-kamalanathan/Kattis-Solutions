import sys
import math
def Sum(n):
    s=0
    while n>0:
        s+=(n%10)
        n=math.floor(n/10)
    return s
def find(n):
    sum_digits=Sum(n)
    p=11
    while True:
        temp=Sum(n*p)
        if temp==sum_digits:
            return p
        p+=1
num=[]
for i in sys.stdin:
    if int(i.strip())==0:
        break
    else:
        t=int(i.strip(" "))
        num.append(t)
res=[]
for i in num:
    r=find(i)
    res.append(r)
for i in res:
    print(i)
