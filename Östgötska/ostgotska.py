n=input().split()
s=0
for i in n:
    if "ae" in i:
        s+=1
if s/len(n)*10<4:
    print("haer talar vi rikssvenska")
else:
    print("dae ae ju traeligt va")
