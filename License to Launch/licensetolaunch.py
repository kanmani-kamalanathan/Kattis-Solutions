n=int(input())
a=input().split()
lst=[]
for i in a:
    lst.append(int(i))
m=min(lst)
print(lst.index(m))
