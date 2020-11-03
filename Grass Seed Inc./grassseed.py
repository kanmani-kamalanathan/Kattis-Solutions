sow=float(input())
n=int(input())
tot=0
while(n>0):
    a,b=list(map(float,input().split()))
    tot+=(a*b*sow)
    n-=1
print(tot)
