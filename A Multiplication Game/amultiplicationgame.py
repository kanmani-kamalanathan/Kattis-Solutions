import sys
from math import ceil

def winner(n):
    player = True
    while n>1:
        d,m = divmod(n,(9 if player else 2))
        n = d+1 if m else d
        player = not player
    return 'Ollie wins.' if player else 'Stan wins.' 

def main():
    print('\n'.join(winner(int(line)) for line in sys.stdin.readlines()))

if __name__ == "__main__":
    main()
