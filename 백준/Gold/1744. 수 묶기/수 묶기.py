import sys
input = sys.stdin.readline


N = int(input())
neg = []
zero = 0
pos = []

for _ in range(N):
    n = int(input())
    if n < 0:
        neg.append(n)
    elif not n:
        zero += 1
    else:
        pos.append(n)

pos.sort(reverse=True)

result = 0
for i in range(len(pos)//2):
    if pos[i * 2] * pos[i * 2 + 1] > pos[i * 2] + pos[i * 2 + 1]:
        result += pos[i * 2] * pos[i * 2 + 1]
    else:
        result += pos[i * 2] + pos[i * 2 + 1]

if len(pos) % 2:
    result += pos[-1]

neg.sort()
if len(neg) > 1:
    for i in range(len(neg)//2):
        result += neg[i * 2] * neg[i * 2 + 1]

    if len(neg) % 2:
        if not zero:
            result += neg[-1]
elif len(neg) == 1:
    if not zero:
        result += neg[0]

print(result)