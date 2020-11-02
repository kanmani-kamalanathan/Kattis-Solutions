from itertools import combinations
dwarf=[]
for i in range(9):
    dwarf.append(int(input()))
poss=list(combinations(dwarf,7))
for j in poss:
    if sum(j)==100:
        ans=j
        break
for i in ans:
    print(i)
