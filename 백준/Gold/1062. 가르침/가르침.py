import sys
from collections import Counter
input = sys.stdin.readline

N, K = map(int, input().split())
words = [Counter(input().strip()) for _ in range(N)]
alpha = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

if K < 5:
    print(0)
elif K == 5:
    teach = ['a', 'n', 't', 'i', 'c']

    answer = 0
    for w in words:
        for k in w.keys():
            if k not in teach:
                break
        else:
            answer += 1

    print(answer)
else:
    teach = ['a', 'n', 't', 'i', 'c']
    n = K - 5
    piece = []
    for w in words:
        for k in w.keys():
            if k not in teach and k not in piece:
                piece.append(k)

    if n >= len(piece):
        print(N)
    else:
        answer = 0
        for i in range(1 << len(piece)):
            result = 0
            add = []
            for j in range(len(piece)):
                if i & (1 << j):
                    add.append(piece[j])

            if len(add) == n:
                for w in words:
                    for k in w.keys():
                        if k not in teach and k not in add:
                            break
                    else:
                        result += 1
                answer = max(answer, result)

        print(answer)