import random
a,b=input().split()
a=int(a)
b=int(b)
lst=list(range(1,a+1))
l=[]
for i in range(b):
    l.append(int(input()))
for i in l:
    if i in lst:
        lst.remove(i)
if lst==[]:
    print("too late")
else:
    print(random.choice(lst))
