from math import pi

A,N = map(float, input().split())
if N**2 / (4*pi) >= A:
    print('Diablo is happy!')
else:
    print('Need more materials!')
