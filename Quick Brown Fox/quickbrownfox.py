alpha=set()
for i in range(0,26):
    alpha.add(chr(97+i))
n=int(input())
while n>0:
    s=input()
    temp=[]
    for i in s:
        if i.isalpha():
            temp.append(i.lower())
    miss=""
    for i in alpha:
        if temp.count(i)==0:
            miss=miss+i.lower()
    if miss=="":
        print('pangram')
    else:
        print('missing',miss)
    n-=1
