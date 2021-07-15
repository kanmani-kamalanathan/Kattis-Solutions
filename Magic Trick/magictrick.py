word=input()
s=set()
c=1
for i in word:
    if i in s:
        c=0
        break
    s.add(i)
print(c)
