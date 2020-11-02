import sys
lst=[]
for i in sys.stdin:
    if i.strip()=="":
        break
    else:
        lst.append(i.strip())
c=1
for i in lst:
    a=i.split()
    b=[]
    for j in a:
        j=int(j)
        b.append(j)
    Max=max(b[1:])
    Min=min(b[1:])
    r=Max-Min
    print("Case","%d:"%c,Min,Max,r)
    c+=1
