T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    if n % h:
        b = n // h + 1
        a = n % h
    else:
        b = n // h
        a = h

    if b < 10:
        print(str(a) + '0' + str(b))
    else:
        print(str(a) + str(b))