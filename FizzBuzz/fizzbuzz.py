#https://open.kattis.com/problems/fizzbuzz

a,b,n=input().split()
a=int(a)
b=int(b)
n=int(n)
for i in range(1,n+1):
    if((i%a==0)and(i%b==0)):
        print("FizzBuzz")
        continue
    elif i%a==0:
        print("Fizz")
        continue
    elif i%b==0:
        print("Buzz")
        continue
    else:
        print(i)
