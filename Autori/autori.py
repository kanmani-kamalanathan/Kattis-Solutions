#https://open.kattis.com/problems/autori

a=input()
txt=a.split('-')
t=''
for i in txt:
    t=t+i[0]
print(t)
