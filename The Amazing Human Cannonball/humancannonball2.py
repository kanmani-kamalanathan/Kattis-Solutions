import math
for i in range(0,int(input())):
    arr = list(map(float, input().split(' ')))
    t = arr[2]/(math.cos(math.pi*arr[1]/180)*arr[0])
    h = arr[0]*math.sin(math.pi*arr[1]/180)*t-(0.5*9.81*t*t)
    print("Safe" if h<=arr[4]-1 and h>=arr[3]+1 else "Not Safe")
