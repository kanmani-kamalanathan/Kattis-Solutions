scoring=input()
p_A,p_B=0,0
def tie_breaker(s,i):
    p_A,p_B=10,10
    for j in range(i,len(s)-1):
        if abs(p_A-p_B)>=2:
            break
        elif s[j]=='A':
            p_A+=int(s[j+1])
        elif s[j]=='B':
            p_B+=int(s[j+1])
    if p_A>p_B:
        print("A")
    else:
        print("B")
        
        
for i in range(0,len(scoring)-1):
    if p_A==10 and p_B==10:
        tie_breaker(scoring,i)
        break
    elif scoring[i]=='A':
        p_A+=int(scoring[i+1])
        if p_A>=11:
            print("A")
            break
    elif scoring[i]=='B':
        p_B+=int(scoring[i+1])
        if p_B>=11:
            print("B")
            break
