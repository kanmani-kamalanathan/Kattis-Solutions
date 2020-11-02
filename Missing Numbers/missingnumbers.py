n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
l=[]
count=0
for i in range(1,lst[-1]+1):
    if i not in lst:
        l.append(i)
        count+=1
if count==0:
    print("good job")
else:
    for i in l:
        print(i)
