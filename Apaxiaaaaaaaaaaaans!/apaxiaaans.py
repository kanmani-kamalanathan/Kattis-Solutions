a=input()
b=a[0]
for i in range(1,len(a)):
    if a[i]!=a[i-1]:
        b+=a[i]
print(b)
