#https://open.kattis.com/problems/parking2

n=int(input())
for i in range(n):
    a=int(input())
    t=input().split()
    test=[int(x) for x in t]
    d=max(test)-min(test)
    print(d*2)
