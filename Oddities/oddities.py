#https://open.kattis.com/problems/oddities

n=int(input())
for i in range(n):
    a=int(input())
    if a%2==0:
        print("%d"%a,"is even")
    else:
        print("%d"%a,"is odd")
