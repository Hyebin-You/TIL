import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    if N == 1:
        print(f'#{tc} {1}')
        continue

    s = []
    for i in range(N):
        s.append((1, [(0, i)], [i]))

    di = [-1, 1, -1, 1]         # 우상, 우하, 좌상, 좌하
    dj = [1, 1, -1, -1]
    result = 0
    while s:
        l_idx, positions, visited = s.pop()
        if l_idx == N:
            result += 1
            continue

        for i in range(N):
            if i not in visited:
                for h in range(4):
                    k = 0
                    status = True
                    while True:
                        nx, ny = l_idx + di[h]*k, i + dj[h]*k
                        if 0 <= nx < N and 0 <= ny < N:
                            if (nx, ny) not in positions:
                                k += 1
                            else:
                                status = False
                                break
                        else:
                            break
                    if not status:
                        break
                else:
                    s.append((l_idx+1, positions + [(l_idx, i)], visited + [i]))

    print(f'#{tc} {result}')



# N이 11까지는 적당한 속도로 계산되지만 그보다 커지면 결과가 나오는데 시간이 꽤 걸리므로
# 다른 방법으로 구현하는 것을 알아보기