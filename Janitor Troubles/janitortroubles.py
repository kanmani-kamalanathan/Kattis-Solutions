a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
s=(a+b+c+d)/2
res=((s-a)*(s-b)*(s-c)*(s-d))**0.5
print(res)
