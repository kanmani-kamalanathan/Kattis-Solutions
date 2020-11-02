lst=[]
lst_cases=[]
dt=input().split(" ")
problems,test_cases=int(dt[0]),int(dt[1])
while problems>0:
    n=test_cases
    while n>0:
        lst.append(input().strip())
        n-=1
    temp=list(lst)
    lst_cases.append(temp)
    lst.clear()
    problems-=1
result=0
for l in lst_cases:
    count=0
    flag=True
    for k in l:
        count=sum(1 for c in k if c.isupper())
        if count>1:
            flag=False
            break
        elif count==1 and not k[0].isupper():
            flag=False
            break
        elif count==0 or (count==1 and k[0].isupper()):
            flag=True
    if flag:
        result+=1
print(result)
