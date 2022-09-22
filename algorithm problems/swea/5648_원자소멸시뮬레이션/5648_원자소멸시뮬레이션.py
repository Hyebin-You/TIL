import sys
sys.stdin = open('sample_input.txt')


def c_or_not(a1, a2):               # 두 원자가 충돌하는지 안하는지, 한다면 언제 충돌하는지
    if a1[0] == a2[0]:
        if a1[1] < a2[1]:       # x 좌표가 같을때 y값이 더 큰게 a1이 되도록
            a1, a2 = a2, a1
    else:
        if a1[0] > a2[0]:
            a1, a2 = a2, a1     # 둘 중 왼쪽에 있는 점이 a1이 되도록

    if a1[0] == a2[0] and (a1[2], a2[2]) == (1, 0):
        time = (a1[1] - a2[1]) / 2
        return time, (a1[0], a1[1] - time)
    elif a1[1] == a2[1] and (a1[2], a2[2]) == (3, 2):
        time = (a2[0] - a1[0]) / 2
        return time, (a2[0] - time, a1[1])
    elif a1[2] == 0:            # 왼쪽 원자가 올라갈때
        if a1[1] < a2[1] and a2[2] == 2:
            if a2[1] - a1[1] == a2[0] - a1[0]:
                return a2[1] - a1[1], (a1[0], a2[1])
    elif a1[2] == 1:            # 왼쪽 원자가 내려갈때
        if a1[1] > a2[1] and a2[2] == 2:
            if a1[1] - a2[1] == a2[0] - a1[0]:
                return a1[1] - a2[1], (a1[0], a2[1])
    elif a1[2] == 3:            # 왼쪽 원자가 오른쪽으로 갈때
        if a2[2] == 0 and a1[1] > a2[1]:        # 오른쪽 원자가 위로 올라가고 a1보다 밑에 있다면
            if a2[0] - a1[0] == a1[1] - a2[1]:
                return a2[0] - a1[0], (a2[0], a1[1])
        elif a2[2] == 1 and a1[1] < a2[1]:
            if a2[0] - a1[0] == a2[1] - a1[1]:
                return a2[0] - a1[0], (a2[0], a1[1])

    return -1, (-1001, -1001)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    # (x, y, 이동방향, 보유 에너지)
    # 이동방향 = {0:상, 1:하, 2:좌, 3:우}
    info_dict = {i:set() for i in range(N)}
    time = []
    time_pos = {}

    for i in range(N):
        for j in range(i+1, N):
            t, point = c_or_not(info[i], info[j])
            if t > 0:
                if t not in time:
                    time.append(t)
                if t not in time_pos.keys():
                    time_pos[t] = {point}
                else:
                    time_pos[t].add(point)
                info_dict[i].add((t, point))
                info_dict[j].add((t, point))

    time.sort()
    result = 0
    b_list = []
    for t in time:
        for p in time_pos[t]:
            r_list = []
            for k, v in info_dict.items():
                if (t, p) in v and k not in b_list:
                    r_list.append(k)
            if len(r_list) > 1:
                for i in r_list:
                    b_list.append(i)
                    result += info[i][3]

    print(f'#{tc} {result}')