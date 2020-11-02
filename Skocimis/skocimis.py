a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
s=b-a
d=c-b
if d>s:
    d-=1
    print(d)
else:
    s-=1
    print(s)
