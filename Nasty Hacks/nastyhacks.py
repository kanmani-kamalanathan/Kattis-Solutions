#https://open.kattis.com/problems/nastyhacks

n = int(input())
for i in range(n):
    case = [int(x) for x in input().split()]
    if (case[1] - case[2] > case[0]):
        print("advertise")
    elif (case[1] - case[2] < case[0]):
        print("do not advertise")
    else:
        print("does not matter")
