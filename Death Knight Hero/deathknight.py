import sys
lst=[]
res=0
count=0
for i in sys.stdin:
    if i.strip()=="":
        break
    if count!=0:
        lst.append(i.strip())
    else:
        res=int(i)
        count+=1
for i in lst:
    if i.__contains__("CD"):
        res-=1
print(res)
