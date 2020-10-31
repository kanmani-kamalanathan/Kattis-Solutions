#https://open.kattis.com/problems/everywhere

n=int(input())
lst=[]
for i in range(n):
    m=int(input())
    d={}
    for j in range(m):
        a=input()
        if a in d:
            d[a]+=1
        else:
            d[a]=1
    lst.append(len(d))
for k in lst:
    print(k)
