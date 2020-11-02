import sys
import math
count=0
lst=[]
for i in sys.stdin:
    if i.strip()=="":
        break
    elif count==0:
        count+=1
    else:
        lst.append(i.strip())
def get_sum(n):
    s=0
    while n>0:
        s=s+n%10
        n=int(math.floor(n/10))
    return s
for k in lst:
    temp=0
    i=len(k)-1
    flag=False
    while i>=0:
        if flag:
            num=int(k[i])*2
            flag=False
            if len(str(num))>1:
                rem=get_sum(num)
                temp=temp+rem
            else:
                temp=temp+num
        else:
            temp=temp+int(k[i])
            flag=True
        i=i-1
    if temp%10==0:
        print("PASS")
    else:
        print("FAIL")
