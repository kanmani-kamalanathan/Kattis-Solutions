#https://open.kattis.com/problems/qaly

n=int(input())
lst=[]
for i in range(n):
    a,b=input().split()
    a=float(a)
    b=float(b)
    res=a*b
    lst.append(res)
s=0
for i in lst:
    s+=i
print(s)
