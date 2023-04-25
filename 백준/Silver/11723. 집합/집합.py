import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    commands = list(input().split())
    if len(commands) == 2:
        cm, n = commands[0], int(commands[1])
    else:
        cm = commands[0]

    if cm == 'add':
        S.add(n)
    elif cm == 'remove' and n in S:
        S.remove(n)
    elif cm == 'check':
        if n in S:
            print(1)
        else:
            print(0)
    elif cm == 'toggle':
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif cm == 'all':
        S = set(range(1, 21))
    elif cm == 'empty':
        S = set()