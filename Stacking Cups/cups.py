n=int(input())
d={}
for i in range(n):
    a=input().split()
    if a[0].isnumeric():
        d[int(a[0])/2]=a[1]
    else:
        d[int(a[1])]=a[0]
for i in sorted(d):
    print(d[i])
