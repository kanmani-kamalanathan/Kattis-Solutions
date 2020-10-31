import sys
count=0
lst=[]
for i in sys.stdin:
    if i.strip()=="":
        break
    elif count==0:
        count+=1
    else:
        lst.append(i)
for i in lst:
    if i[0]=="P":
        print("skipped")
    else:
        t=i.split("+")
        print(int(t[0])+int(t[1]))
