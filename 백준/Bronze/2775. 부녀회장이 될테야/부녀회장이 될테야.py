T = int(input())

rooms = [[i for i in range(15)]]

for _ in range(T):
    k = int(input())
    n = int(input())

    if k < len(rooms):
        print(rooms[k][n])
    else:
        while k >= len(rooms):
            floor = [0] * 15
            for i in range(14):
                floor[i + 1] = floor[i] + rooms[-1][i+1]
            rooms.append(floor)

        print(rooms[k][n])