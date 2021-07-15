n=int(input())
for i in range(n):
    s=input()
    if "simon says" in s:
        print(s[11:])
    else:
        print(" ")
