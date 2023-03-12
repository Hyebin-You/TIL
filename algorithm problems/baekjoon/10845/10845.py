from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    command = input().split()
    if len(command) == 2:
        q.append(command[1])
    elif command[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    else:
        if len(q):
            print(q[-1])
        else:
            print(-1)