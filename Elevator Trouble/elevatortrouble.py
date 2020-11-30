f,s,g,u,d=list(map(int,input().split()))
push=0
going=s
while (g>going) and u>0:
    going=going+u
    push+=1
while (going>g) and d>0:
    going=going-d
    push+=1
if g==going:
    print(push)
else:
    print("use the stairs")
