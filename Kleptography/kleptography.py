lastlen, plainlen = list(map(int, input().split()))
last = input()
cipher = input()
output = last[::-1]
count = 0
for i in range (plainlen-1,lastlen-1,-1):
    tmp = 97 + (ord(cipher[i]) - ord(output[count]))%26
    output += chr(tmp)
    count += 1
print(output[::-1])
