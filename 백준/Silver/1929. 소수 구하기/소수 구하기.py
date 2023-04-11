def isPrime(num):
    for i in range(2, int(num**(1/2)) + 1):
        if not num % i:
            return False

    return True


M, N = map(int, input().split())
for n in range(M, N + 1):
    if n == 1:
        continue
    if isPrime(n):
        print(n)