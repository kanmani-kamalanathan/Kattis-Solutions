a=input()
l=len(a)//3
x=a[0:l]
y=a[l:l*2]
z=a[l*2:len(a)]
if (x==y):
  print(x)
else:
  print(z)
