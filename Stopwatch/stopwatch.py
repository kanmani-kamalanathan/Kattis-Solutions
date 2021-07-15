n=int(input())
a=[]
time=0
for i in range(n):
    a.append(int(input()))
if n%2==0:
    for i in range(0,n-1,2):
        time+=(a[i+1]-a[i])
    print(time)
else:
    print("still running")
