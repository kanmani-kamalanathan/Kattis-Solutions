#https://open.kattis.com/problems/spavanac

h,m=input().split()
h=int(h)
m=int(m)
if m>45:
    print(str(h),str(m-45))
else:
    if h!=0:
        print(str(h-1),str((m+60)-45))
    else:
        print("23",str((m+60)-45))
