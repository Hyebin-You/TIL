N = int(input())
arr = list(map(int, input().split()))

arr.sort()
sums = 0

for i in range(N):
    sums += sum(arr[:i+1])

print(sums)