n,v=input().split()
n=int(n)
v=int(v)
lst=[]
for i in range(n):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d=a*b*c
    lst.append(d)
res=max(lst)-v
print(res)
