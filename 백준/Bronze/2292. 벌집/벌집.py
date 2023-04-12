N = int(input())

if N == 1:
    print(1)
else:
    i = 1
    rooms = 1
    while True:
        rooms += 6 * i
        if N <= rooms:
            break
        else:
            i += 1
    print(i + 1)