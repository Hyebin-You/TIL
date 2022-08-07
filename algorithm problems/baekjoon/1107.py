channel = int(input())
wrong_num = int(input())
if wrong_num:
    wrong_nums = list(map(int, input().split()))
else:
    wrong_nums = []

min_distance = abs(100 - channel)

for i in range(1000001):
    for j in range(len(str(i))):
        if int(str(i)[j]) in wrong_nums:
            break
        elif j == len(str(i)) - 1:
            min_distance = min(min_distance, abs(i - channel) + len(str(i)))

print(min_distance)