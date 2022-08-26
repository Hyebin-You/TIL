import sys
sys.stdin = open('sample_in.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_info = [list(map(int, input().split())) for _ in range(N)]
    station = [0] * 1001

    for bus in bus_info:
        if bus[0] == 1:
            for i in range(bus[1], bus[2]+1):
                station[i] += 1
        elif bus[0] == 2:
            for i in range(bus[1], bus[2], 2):
                station[i] += 1
            station[bus[2]] += 1
        else:
            if bus[1]%2:
                for i in range(bus[1] + 1, bus[2]):
                    if not i%3 and i%10:
                        station[i] += 1
                station[bus[2]] += 1
                station[bus[1]] += 1
            else:
                for i in range(bus[1]+1, bus[2]):
                    if not i%4:
                        station[i] += 1
                station[bus[1]] += 1
                station[bus[2]] += 1

    print(f'#{tc} {max(station)}')