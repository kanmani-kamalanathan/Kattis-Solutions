line=['1']*int(input())
l=len(line)
i=2
for num in list(map(int,input().split())):
    line[1+num]=str(i)
    i=i+1
print(" ".join(line))
