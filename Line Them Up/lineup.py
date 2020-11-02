n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
if lst==sorted(lst):
    print("INCREASING")
elif lst==sorted(lst)[::-1]:
    print("DECREASING")
else:
    print("NEITHER")
