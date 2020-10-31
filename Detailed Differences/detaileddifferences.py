n=int(input())
lst=[]
res=[]
for i in range(0,n*2):
    lst.append(input())
for i in range(1,n*2+1):
    if i%2!=0:
        r=""
        for j in range(len(lst[i-1])):
            if lst[i-1][j]==lst[i][j]:
                r=r+"."
            else:
                r=r+"*"
        res.append(r)
for i in range(1,n*2+1):
    if i%2!=0:
        print(lst[i-1])
        print(lst[i])
        print(res[i//2])
        print("")
