print((lambda s, k: 'Yes' if ''.join(sorted(s))[len(s)-k:k] == s[len(s)-k:k] else 'No')(*(lambda a,b: (a,int(b)))(*input().split())))
