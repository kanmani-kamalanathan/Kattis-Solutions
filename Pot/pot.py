#https://open.kattis.com/problems/pot

n=int(input())
c=[]
x=0
for i in range(0,n):
    c.append(int(input()))
for i in c:
    a=i%10
    b=i//10
    x+=(b**a)
print(x)
