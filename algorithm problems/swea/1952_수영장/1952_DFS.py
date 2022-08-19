import sys
sys.stdin = open('sample_input.txt')


def dfs_save_money(month, cost):
    global min_cost
    if min_cost <= cost:
        return

    if month > 11:
        min_cost = cost
        return

    if month_plan[month] != 0:
        dfs_save_money(month + 1, cost + dm*month_plan[month])
        dfs_save_money(month + 1, cost + mm)
        dfs_save_money(month + 3, cost + mm3)
    else:
        dfs_save_money(month + 1, cost)


T = int(input())
for tc in range(1, T+1):
    dm, mm, mm3, ym = map(int, input().split())
    month_plan = list(map(int, input().split()))

    min_cost = ym
    dfs_save_money(0, 0)
    print(f'#{tc} {min_cost}')