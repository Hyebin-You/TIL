switch_num = int(input())
switch = list(map(int, input().split()))
p_num = int(input())
p_info = [tuple(map(int, input().split())) for _ in range(p_num)]

for p in p_info:
    if p[0] == 1:       # 남학생이라면
        for i in range(switch_num):
            if not (i+1) % p[1]:
                if switch[i]:
                    switch[i] = 0
                else:
                    switch[i] = 1
    else:               # 여학생이라면
        if switch[p[1]-1]:
            switch[p[1]-1] = 0
        else:
            switch[p[1] - 1] = 1
        j = 1
        while True:
            if 0 <= p[1] - 1 - j and p[1] - 1 + j < switch_num:
                if switch[p[1] - 1 - j] == switch[p[1] - 1 + j]:
                    if switch[p[1] - 1 - j]:
                        switch[p[1] - 1 - j] = 0
                    else:
                        switch[p[1] - 1 - j] = 1
                    if switch[p[1] - 1 + j]:
                        switch[p[1] - 1 + j] = 0
                    else:
                        switch[p[1] - 1 + j] = 1
                    j += 1
                else:
                    break
            else:
                break
if switch_num <= 20:
    print(*switch)
elif 20 < switch_num <= 41:
    print(*switch[0:20])
    print(*switch[20:])
elif 40 < switch_num <= 60:
    print(*switch[0:20])
    print(*switch[20:40])
    print(*switch[40:])
elif 60 < switch_num <= 80:
    print(*switch[0:20])
    print(*switch[20:40])
    print(*switch[40:60])
    print(*switch[60:])
else:
    print(*switch[0:20])
    print(*switch[20:40])
    print(*switch[40:60])
    print(*switch[60:80])
    print(*switch[80:])