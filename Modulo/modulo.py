n=[]
a=[]
for i in range(1,11):
    n.append(int(input()))
for i in n:
    x=i%42
    if x not in a:
        a.append(x)
print(len(a))
