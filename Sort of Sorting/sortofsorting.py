n=int(input())
f=True
while n:
    if not f:
        print(" ")
    name=[input() for _ in range(n)]
    name.sort(key = lambda x: x[:2])
    print("\n".join(name))
    n=int(input())
    f=False
