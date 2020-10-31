#https://open.kattis.com/problems/pieceofcake2

t=4
n,h,v=input().split()
n=int(n)
h=int(h)
v=int(v)
a=n-h
b=n-v
if(((a>h) or(a==h)) and ((b>v) or (b==v))):
    V=a*b*t
elif(((a>h) or (a==h)) and ((b<v) or (b==v))):
    V=a*v*t
elif(((a<h) or (a==h))and ((b>v)or (b==v))):
    V=h*b*t
else:
    V=h*v*t
print(V)
