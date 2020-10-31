#https://open.kattis.com/problems/cold

n=int(input())
a=input().split()
z=[]
count=0
for i in a:
    i=int(i)
    z.append(i)
for i in z:
    if i<0:
        count+=1
print(count)
