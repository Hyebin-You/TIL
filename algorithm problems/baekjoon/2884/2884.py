h, m = map(int, input().split())
if m >= 45:
    m -= 45
else:
    if h == 0:
        h = 23
        m += 15
    else:
        h -= 1
        m = m + 15

print(h, m)