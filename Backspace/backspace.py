n=input()
res=[]
for i in n:
    if i=="<" and len(res)>0:
        res.pop()
    else:
        res.append(i)
print("".join(res))
