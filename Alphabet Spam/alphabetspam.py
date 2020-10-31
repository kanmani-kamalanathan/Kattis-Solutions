n=input()
lc=0
uc=0
ws=0
s=0
a=len(n)
for i in n:
    if i=="_":
        ws+=1
    elif i.isupper()==True:
        uc+=1
    elif i.islower()==True:
        lc+=1
    else:
        s+=1
print(float(ws/a))
print(float(lc/a))
print(float(uc/a))
print(float(s/a))
