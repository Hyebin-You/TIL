p_num = int(input())
people = []
for i in range(p_num):
    people.append(tuple(map(int, input().split())))

for i in range(len(people)):
    count = 0
    for j in range(len(people)):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    print(count + 1, end= ' ')