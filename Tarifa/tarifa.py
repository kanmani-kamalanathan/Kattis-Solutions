#https://open.kattis.com/problems/tarifa

x=int(input())
n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
s=sum(a)
tot=x*(n+1)
t=tot-s
print(t)
