n=int(input())
while(True):
    copy=n
    s=0
    while(copy!=0):
        i=copy%10
        s+=i
        copy//=10
    if(n%s==0):
        break
    n+=1
print(n)
