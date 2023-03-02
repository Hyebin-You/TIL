def gcd_num(a, b):
    while True:
        if not a % b:
            break

        a, b = b, a % b

    return b

a, b = map(int, input().split())
print(gcd_num(a, b))
print(a * b // gcd_num(a, b))