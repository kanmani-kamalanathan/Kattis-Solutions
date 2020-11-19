n=int(input())
for i in range(n):
    input()
    amt=[int(x) for x in input().split()]
    g=[int(x) for x in input().split()]
    m=[int(x) for x in input().split()]
    print("Godzilla" if max(g)>=max(m) else "MechaGodzilla")
