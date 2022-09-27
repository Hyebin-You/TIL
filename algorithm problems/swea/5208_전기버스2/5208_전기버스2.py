import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    s = [(1, arr[1], 0)]
    result = arr[0]
    while s:
        idx, b, cnt = s.pop()
        if idx + b >= arr[0]:
            if cnt < result:
                result = cnt
            continue
        if cnt > result:
            continue
        for i in range(1, b+1):
            s.append((idx+i, arr[idx+i], cnt+1))

    print(f'#{tc} {result}')