import sys
for i in sys.stdin:
    if i.strip()==" ":
        break
    else:
        a=i.split()
        lst=[]
        for j in a:
            j=int(j)
            lst.append(j)
        s=sum(lst)
        for k in lst:
            if (2*k)==s:
                print(k)
                break
