import sys
input = sys.stdin.readline


def check(ar):
    check_ar = ''
    for l in ar:
        for w in l:
            check_ar += w

    if '1' in check_ar and '0' not in check_ar:
        return 1
    elif '0' in check_ar and '1' not in check_ar:
        return 0
    else:
        return -1


def count_paper(ar, n):
    global cnt_b
    global cnt_w

    if check(ar) == 1:
        cnt_b += 1
    elif not check(ar):
        cnt_w += 1
    else:
        ar1 = [ar[i][0:n//2] for i in range(n//2)]
        ar2 = [ar[i][n//2:] for i in range(n//2)]
        ar3 = [ar[i][0:n//2] for i in range(n//2, n)]
        ar4 = [ar[i][n//2:] for i in range(n//2, n)]

        count_paper(ar1, n//2)
        count_paper(ar2, n//2)
        count_paper(ar3, n//2)
        count_paper(ar4, n//2)


N = int(input())
arr = [input().split() for _ in range(N)]

cnt_w = 0
cnt_b = 0

count_paper(arr, N)

print(cnt_w)
print(cnt_b)