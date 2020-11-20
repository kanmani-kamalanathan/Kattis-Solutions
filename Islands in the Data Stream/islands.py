n=int(input())
for i in range(n):
    a=list(map(int,input().split()))
    l=a[1:]
    count=0
    j=1
    while j<len(l):
        k=j+1
        while k<len(l):
            temp=l[j:k]
            if min(temp)>l[j-1] and min(temp)>l[k]:
                count+=1
            k+=1
        j+=1
    print(a[0],count)
