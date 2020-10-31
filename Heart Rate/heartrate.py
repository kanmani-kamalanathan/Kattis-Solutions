#https://open.kattis.com/problems/heartrate

n=int(input())
for _ in range(n):
    b,p=list(map(float,input().split()))
    bmin=60/(p/(b-1))
    bpm=60*b/p
    bmax=60/(p/(b+1))
    print(float(round(bmin,4)),float(round(bpm,4)),float(round(bmax,4)))
