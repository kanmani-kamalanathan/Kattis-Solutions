import sys
for line in sys.stdin:
    if line.strip()!='0':
        dt=list(map(float,line.split()))
        x1,y1,x2,y2,p=float(dt[0]),float(dt[1]),float(dt[2]),float(dt[3]),float(dt[4])
        res=pow(pow(abs(x1-x2),p)+pow(abs(y1-y2),p),1/p)
        print(res)
