n=int(input())
while(n!=-1):
    d=0
    sp=[]
    ti=[]
    diff=[]
    for i in range(n):
        x=input().split()
        sp.append(int(x[0]))
        ti.append(int(x[1]))
    diff.append(ti[0])
    for j in range(1,len(ti)):
        diff.append(ti[j]-ti[j-1])
    for k in range(len(sp)):
        d+=(sp[k]*diff[k])
    print("%d miles"%d)
    n=int(input())
