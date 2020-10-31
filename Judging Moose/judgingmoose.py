a,b=input().split()
a=int(a)
b=int(b)
if ((a!=0) & (b!=0) & (a==b)):
    print("Even ",a*2)
elif a>b:
    print("Odd ",a*2)
elif b>a:
    print("Odd ",b*2)
else:
    print("Not a moose")
