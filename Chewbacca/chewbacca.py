from math import ceil

def least_common_ancestor(k,a,b):
    s,a,b = 0,a-1,b-1
    while a != b:
        if a > b:
            a = ceil(a/k)-1
        else:
            b = ceil(b/k)-1
        s += 1
    return s

_,k,q = map(int,input().split())
print('\n'.join(str(least_common_ancestor(k,*map(int,input().split()))) for _ in range(q)))
