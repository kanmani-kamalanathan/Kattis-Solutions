import sys
Min=sys.maxsize
n=int(input())
flag=False
cans=sys.stdin.readline()
can=list(map(int,cans.split()))
can.sort()
for i in range(n):
    if i+1<can[i]:
        flag=True
        break
    F=can[i]/float(i+1)
    if Min>F:
        Min=F
if flag==False:
    print(Min)
else:
    print("impossible")
