n=list(map(int,input().split()))
n.sort()
d1=n[1]-n[0]
d2=n[2]-n[1]
if d1==d2:
    print(n[2]+d1)
elif d1>d2:
    print(n[0]+d2)
else:
    print(n[1]+d1)
