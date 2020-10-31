n=int(input())
a=[]
for i in range(n):
    s,t=input().split()
    s=int(s)
    t=int(t)
    for j in range(s,t+1):
        if j not in a:
            a.append(j)
print(len(a))
