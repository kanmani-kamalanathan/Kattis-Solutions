a=input().split(';')
c=0
for i in a:
    if '-' in i:
        t=list(map(int,i.split('-')))
        c+=(t[1]-t[0]+1)
    else:
        c+=1
print(c)
