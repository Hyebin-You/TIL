import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    V, E = map(int, input().split())
    line_info = list(map(int, input().split()))
    a = [(i, []) for i in range(1, V+1)]
    line_dict = dict(a)

    for i in range(E):
        line_dict[line_info[i*2+1]].append(line_info[i*2])
    print(line_dict)

    q = []
    for k, v in line_dict.items():
        if not len(v):
            q.append(k)

    result = []
    while q:
        t = q.pop(0)
        result.append(t)
        for k, v in line_dict.items():
            if t in v:
                v.remove(t)
                line_dict[k] = v
                if not len(v):
                    q.append(k)

    print(f'#{tc}', *result)