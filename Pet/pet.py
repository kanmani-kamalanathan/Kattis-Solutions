#https://open.kattis.com/problems/pet

br,bs=-1,-1
for i in range(5):
    a,b,c,d=input().split()
    a,b,c,d=int(a),int(b),int(c),int(d)
    score=a+b+c+d
    if score>bs:
        br=i+1
        bs=score
print("%d %d"%(br,bs))
