def valid(words):
    for i, w in enumerate(words):
        if not w.startswith('m') and i+1 != int(w):
            return False
    return True
    
int(input())
print('makes sense' if valid(input().split()) else 'something is fishy')
