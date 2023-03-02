def isprime(n):
    if n == 1:
        return False

    for i in range(2, int(n**(1/2)) + 1):
        if not n % i:
            return False
    else:
        return True


N = int(input())
nums = list(map(int, input().split()))
result = 0

for n in nums:
    if isprime(n):
        result += 1

print(result)