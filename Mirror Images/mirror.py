n=int(input())
for i in range(n):
    case=i+1
    a=input().split()
    lst=[]
    for j in range(int(a[0])):
        lst.append(input())
    print("Test "+str(case))
    for k in lst[::-1]:
        print(k[::-1])
