from itertools import permutations
n=input()
perms=[''.join(p) for p in permutations(n)]
big=[]
for i in perms:
    if int(i)>int(n):
        big.append(int(i))
if len(big)>0:
    print(min(big))
else:
    print("0")
