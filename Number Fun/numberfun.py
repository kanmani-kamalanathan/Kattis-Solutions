n=int(input())
for i in range(n):
    s=input().split()
    lst=[]
    for j in s:
        lst.append(int(j))
    a,b,c=lst
    if(a+b==c or a-b==c or b-a==c or a*b==c or a/b==c or b/a==c):
        print("possible")
    else:
        print("impossible")
