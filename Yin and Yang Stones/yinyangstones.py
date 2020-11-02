n=input()
w=b=0
for i in range(len(n)):
    if n[i]=="W":
        w+=1
    else:
        b+=1
if((w>b)|(b>w)):
    print("0")
else:
    print("1")
