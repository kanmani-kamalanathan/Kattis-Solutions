n=int(input())
wrong=[]
correct=[" "]
for i in range(n):
    s=input()
    wrong.append(s)
    correct.append(s)
c=0
for i in range(1,n):
    if wrong[i]==correct[i]:
        c+=1
print(c)
