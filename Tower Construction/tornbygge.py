n=int(input())
a=list(map(int,input().split()))
tower=1
for i,j in enumerate(a[:-1]):
    if j<a[i+1]:
        tower+=1
print(tower)
