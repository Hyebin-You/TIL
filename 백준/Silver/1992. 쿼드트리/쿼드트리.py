import sys
input = sys.stdin.readline


def check(ar, n):
    in_num = ar[0][0]
    for l in ar:
        if l.count(in_num) != n:
            a = check([ar[i][:n//2] for i in range(n//2)], n//2)
            b = check([ar[i][n//2:] for i in range(n//2)], n//2)
            c = check([ar[i][:n//2] for i in range(n//2, n)], n//2)
            d = check([ar[i][n//2:] for i in range(n//2, n)], n//2)
            return "(" + a + b + c + d + ")"
    else:
        return in_num


N = int(input())

pic = [list(input().rstrip()) for _ in range(N)]
print(check(pic, N))