n=int(input())
a=list(map(int,input().split()))
count=1
res=[str(a[0])]
for i in range(1,len(a)):
    if a[i]>int(res[-1]):
        res.append(str(a[i]))
        count+=1
print(count)
print(" ".join(res))
