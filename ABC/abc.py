a,b,c=input().split()
s=input()
a=int(a)
b=int(b)
c=int(c)
z=[a,b,c]
z.sort()
for i in s:
    if i=='A':
        A=z[0]
    elif i=='B':
        B=z[1]
    else:
        C=z[2]
for i in s:
    if i=='A':
        print(A,'')
    elif i=='B':
        print(B,'')
    else:
        print(C,'')  
