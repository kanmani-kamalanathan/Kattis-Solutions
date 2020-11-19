import sys
for i in sys.stdin:
    if i.strip()=='':
        break
    else:
        a,b=i.split()
        a=float(a)
        b=float(b)
        c=a-b
        print(abs(c))
