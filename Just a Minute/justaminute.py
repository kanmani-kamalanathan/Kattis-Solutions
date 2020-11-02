n=int(input())
m=[]
s=[]
for i in range(n):
    a,b=input().split()
    m.append(int(a))
    s.append(int(b))
M=sum(m)
S=sum(s)
c=S/M
res=c/60
if res<=1:
    print("measurement error")
else:
    print(round(res, 9))
