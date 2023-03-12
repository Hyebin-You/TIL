from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        q.appendleft(command[1])
    elif command[0] == 'push_back':
        q.append(command[1])
    elif command[0] == 'pop_front':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(q):
            print(q.pop())
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