#https://open.kattis.com/problems/quickestimate

n=int(input())
lst=[]
for i in range(n):
    a=int(input())
    a=str(a)
    lst.append(len(a))
for i in lst:
    print(i)
