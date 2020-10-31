i=input().split()
a,b=int(i[0]),int(i[1])
while(a!=0 and b!=0):
    quo=a//b
    rem=a%b
    print(quo,rem,"/",b)
    i=input().split()
    a,b=int(i[0]),int(i[1])
