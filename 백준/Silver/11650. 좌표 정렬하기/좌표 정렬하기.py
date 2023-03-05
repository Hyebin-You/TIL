N = int(input())
points = []

for _ in range(N):
    points.append(list(map(int, input().split())))

points.sort(key=lambda x: (x[0], x[1]))
for i in points:
    print(i[0], i[1])