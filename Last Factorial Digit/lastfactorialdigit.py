#https://open.kattis.com/problems/lastfactorialdigit

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
        
n=int(input())
lst=[]
for i in range(n):
    a=int(input())
    f=fact(a)
    lst.append(f%10)
for i in lst:
    print(i)
