[print('\n'.join(map(lambda w: w[1], sorted([tuple((lambda s: [''.join((lambda lst: lst + ['1' for i in range(10 - len(lst))])(list(map(lambda z: '0' if z[0] == 'u' else '1' if z[0] == 'm' else '2', reversed(s[1].split("-")))))), s[0][:-1]])(input().split())) for j in range(int(input()))]))) + '\n' + ('=' * 30)) for t in range(int(input()))]
