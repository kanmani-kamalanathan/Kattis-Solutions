#https://open.kattis.com/problems/batterup

n=int(input())
a=input().split()
lst=[]
count=0
s=0
for i in a:
    lst.append(int(i))
for i in lst:
    if i>=0:
        s+=i
        count+=1
print(s/count)
