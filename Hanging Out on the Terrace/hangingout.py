dt=input().split()
lim,ev=int(dt[0]),int(dt[1])
c,n,r=0,0,0
for i in range(ev):
    b,n=input().split()
    n=int(n)
    if b[0]=='e':
        if ((c+n)>lim):
            r+=1
        else:
            c+=n
    else:
        c-=n
print(r)
