#https://open.kattis.com/problems/chanukah

n=int(input())
for i in range(n):
    a,b=input().split()
    b=int(b)
    s=0
    for j in range(1,b+1):
        s+=j
    s+=b
    print(a,str(s))
