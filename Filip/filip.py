#https://open.kattis.com/problems/filip

a,b=input().split()
a=int(a)
b=int(b)
c=[0,0]
j=0
for i in (a,b):
    while i>0:
        rem=i%10
        c[j]=(c[j]*10)+rem
        i=i//10
    j=j+1
if c[0]>c[1]:
    print(c[0])
else:
    print(c[1])
