import sys
input = sys.stdin.readline


def check(ar, n):
    global first
    global second
    global third

    in_num = ar[0][0]
    for l in ar:
        if l.count(in_num) != n:
            k = n // 3
            for i in range(1, 4):
                check([ar[j][:k] for j in range(k * (i-1), k * i)], k)
                check([ar[j][k:2*k] for j in range(k * (i-1), k * i)], k)
                check([ar[j][2*k:k*3] for j in range(k * (i-1), k * i)], k)
            return
    else:
        if in_num == -1:
            first += 1
        elif not in_num:
            second += 1
        else:
            third += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
first = 0
second = 0
third = 0
check(paper, N)

print(first)
print(second)
print(third)