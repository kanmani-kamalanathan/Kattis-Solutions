n=int(input())
num=1
while (n>0):
    d={}
    for i in range(0,n):
        a=input()
        a=a.split()
        a=a[len(a)-1].lower()
        if a in d.keys():
            d[a]+=1
        else:
            d.update({a:1})
    print("List "+str(num)+":")
    for ani in sorted(d.keys()):
        print(ani+" | "+str(d[ani]))
    num+=1
    n=int(input())
