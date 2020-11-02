a,b=input().split()
a=int(a)
b=int(b)
c=b-a
if c>1:
    print("Dr. Chaz will have",c,"pieces of chicken left over!")
elif c==1:
    print("Dr. Chaz will have",c,"piece of chicken left over!")
elif c==-1:
    c=abs(c)
    print("Dr. Chaz needs",c,"more piece of chicken!")
else:
    c=abs(c)
    print("Dr. Chaz needs",c,"more pieces of chicken!")
