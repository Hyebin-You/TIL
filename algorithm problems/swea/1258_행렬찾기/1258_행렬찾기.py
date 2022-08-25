import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    storage = []

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                if (i - 1 < 0 and j - 1 < 0) or (i - 1 < 0 and not arr[i][j - 1]) or (not arr[i - 1][j] and j - 1 < 0) or (not arr[i-1][j] and not arr[i][j-1]):
                    a = b = 0
                    while True:
                        b += 1
                        if j + b < n and arr[i][j + b]:
                            pass
                        else:
                            b -= 1
                            break
                    while True:
                        a += 1
                        if i + a < n and arr[i + a][j]:
                            pass
                        else:
                            a -= 1
                            break
                    storage.append(((a+1)*(b+1), a+1, b+1))

    storage.sort(key= lambda i:i[1])
    storage.sort(key= lambda i:i[0])
    result = []
    for box in storage:
        result.extend((box[1], box[2]))

    print(f'#{tc}', len(storage), *result)