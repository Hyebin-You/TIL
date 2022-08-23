def namugi(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a**2) % c
    else:
        if b % 2:
            return (namugi(a, b//2, c)**2 * (a%c))%c
        else:
            return (namugi(a, b//2, c) ** 2) % c


A, B, C = map(int, input().split())
print(namugi(A, B, C))