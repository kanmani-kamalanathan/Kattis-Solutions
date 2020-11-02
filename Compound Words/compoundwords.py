import sys
lst=[]
for i in sys.stdin:
    if i.strip()==" ":
        break
    dt=i.split()
    lst=lst+dt
result=set()
for i in range(len(lst)):
    for j in range(len(lst)):
        if i!=j:
            a=lst[i]+lst[j]
            if a not in result:
                result.add(a)
s=list(result)
s.sort()
for i in s:
    print(i)
