a=input()
count=0
day=0
for i in a:
    if count==0 and i!='P':
        day+=1
    elif count==1 and i!='E':
        day+=1
    elif count==2 and i!='R':
        day+=1
        count=-1
    elif count==2:
        count=-1
    count+=1
print(day)
