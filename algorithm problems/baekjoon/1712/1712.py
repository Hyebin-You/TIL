A, B, C, = map(int, input().split())

if C - B > 0:
    i = A // (C - B) + 1
    if i <= 0:
        i = -1
else:
    i = -1
print(i)