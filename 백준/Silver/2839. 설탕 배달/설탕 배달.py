N = int(input())

five = N // 5
answers = []

for i in range(five + 1):
    if i:
        k = N - 5 * i
        if not k % 3:
            answers.append(i + k // 3)
    else:
        if not N % 3:
            answers.append(N // 3)

if len(answers):
    print(min(answers))
else:
    print(-1)