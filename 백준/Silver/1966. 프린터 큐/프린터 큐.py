import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    documents = deque(list(map(int, input().split())))
    if N == 1:
        print(1)
    else:
        result = 1
        idx = M
        while True:
            if not idx:
                if documents[idx] == max(documents):
                    break
                else:
                    documents.append(documents.popleft())
                    idx = len(documents) - 1
            else:
                if documents[0] == max(documents):
                    documents.popleft()
                    idx -= 1
                    result += 1
                else:
                    documents.append(documents.popleft())
                    idx -= 1
        print(result)