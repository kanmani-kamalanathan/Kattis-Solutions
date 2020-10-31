n=int(input())
count=0
for i in range(n):
    a=input().lower()
    if "pink" in a:
        count+=1
        continue
    elif "rose" in a:
        count+=1
if count!=0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
