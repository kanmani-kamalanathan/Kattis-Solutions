n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=input().split()
    lst=[]
    for j in b:
        lst.append(int(j))
    miss={}
    for j in lst:
        if j not in miss:
            miss[j]=1
        else:
            miss[j]+=1
    for j in miss:
        if miss[j]==1:
            print("Case #%d: %d"%(i,j))
