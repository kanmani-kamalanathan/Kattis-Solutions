#https://open.kattis.com/problems/trik

cups = [True, False, False]
moves = input()
for i in range(len(moves)):
    move = moves[i]
    if move == 'A':
        temp = cups[0]
        cups[0] = cups[1]
        cups[1] = temp
    if move == 'B':
        temp = cups[1]
        cups[1] = cups[2]
        cups[2] = temp
    if move == 'C':
        temp = cups[0]
        cups[0] = cups[2]
        cups[2] = temp
cup=0
for i in range(3):
    if cups[i]:
        cup = i + 1
        break;
print(cup)
