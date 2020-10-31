#https://open.kattis.com/problems/zamka

def digits(n):
    s=0
    while n!=0:
        s+=(n%10)
        n=n//10
    return s
l=int(input())
d=int(input())
x=int(input())
N=0
M=0
for i in range(l,d+1):
    if digits(i)==x:
        N=i
        break
for j in range(d,l-1,-1):
    if digits(j)==x:
        M=j
        break
print(N)
print(M)
