import sys
sys.stdin = open('sample_input.txt')


def turn_magnet(n, h):
    turn_with = {1:[2], 2:[1, 3], 3:[2, 4], 4:[3]}
    q = [(n, h)]
    move = []
    while q:
        s, hh = q.pop(0)
        if s not in move:
            move.append((s, hh))
            for t in turn_with[s]:
                if t > s and magnets[s][2] != magnets[t][6] and (t, -hh) not in move:
                    q.append((t, -hh))
                elif t < s and magnets[s][6] != magnets[t][2] and (t, -hh) not in move:
                    q.append((t, -hh))

    for m in move:
        if m[1] == 1:       # 시계방향 회전이라면
            magnets[m[0]] = [magnets[m[0]][-1]] + magnets[m[0]][:7]
        else:
            magnets[m[0]] = magnets[m[0]][1:] + [magnets[m[0]][0]]


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnets = [[0]] + [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        a, b = map(int, input().split())
        turn_magnet(a, b)

    result = 0
    if magnets[1][0]:   # S극이라면
        result += 1
    if magnets[2][0]:
        result += 2
    if magnets[3][0]:
        result += 4
    if magnets[4][0]:
        result += 8

    print(f'#{tc} {result}')