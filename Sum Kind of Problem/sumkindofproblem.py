n=int(input())
for i in range(n):
    S=[]
    dt=input().split()
    a,b=int(dt[0]),int(dt[1])
    s=0
    for j in range(1,b+1):
        s+=j
    S.append(s)
    s=0
    for j in range(1,b*2+1,2):
        s+=j
    S.append(s)
    s=0
    for j in range(2,b*2+1,2):
        s+=j
    S.append(s)
    print("%d "%a)
    for k in S:
        print("%d "%k)
