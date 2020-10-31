g=list(map(int,input().split()))
e=list(map(int,input().split()))
G=0
E=0
for i in g:
    G+=i
for i in e:
    E+=i
if G==E:
    print("Tie")
elif G>E:
    print("Gunnar")
else:
    print("Emma")
