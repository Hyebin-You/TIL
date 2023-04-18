import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    ar = input().rstrip()
    ar = ar[1:-1]
    if len(ar):
        ar = deque(list(ar.split(',')))
    else:
        ar = deque([])

    reverse = False

    for w in p:
        if w == 'R':
            reverse = not reverse
        else:
            if len(ar):
                if reverse:
                    ar.pop()
                else:
                    ar.popleft()
            else:
                print('error')
                break
    else:
        if reverse:
            ar = list(ar)[::-1]
            print('[' + ','.join(ar) + ']')
        else:
            ar = list(ar)
            print('[' + ','.join(ar) + ']')