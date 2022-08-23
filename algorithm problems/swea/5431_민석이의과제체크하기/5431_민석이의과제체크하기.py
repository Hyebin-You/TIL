import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    people = list(range(N))
    result = []
    for i in people:
        if i + 1 not in arr:
            result.append(i+1)

    print(f'#{tc}', *result)