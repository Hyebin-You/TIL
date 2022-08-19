import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    dm, mm, mm3, ym = map(int, input().split())
    month_plan = list(map(int, input().split()))
    final_plan = [0] * 12

    dm_list = [dm * i for i in month_plan]
    for i in range(12):  # 1달 가격과 일 가격 비교
        if month_plan[i] * dm < mm:
            final_plan[i] = month_plan[i] * dm
        else:
            final_plan[i] = mm

    sum_3m = [final_plan[i] + final_plan[i + 1] + final_plan[i + 2] for i in range(10)]
    result = sum(final_plan)
    if max(sum_3m) < mm3:
        if result < ym:
            print(f'#{tc} {result}')
        else:
            result = ym
            print(f'#{tc} {result}')
    else:
        # 3달짜리 썼을 때 절약되는 값들 계산 ( 그 중 최댓값 찾기)
        # 3달짜리가 1개일때
        save_m = max(sum_3m) - mm3

        # 3달짜리가 2개일때
        for i in range(7):
            for j in range(i + 3, 10):
                if (sum_3m[i] + sum_3m[j] - mm3 * 2) > save_m:
                    save_m = (sum_3m[i] + sum_3m[j] - mm3 * 2)

        # 3달짜리가 3개일때
        for i in range(4):
            for j in range(i + 3, 7):
                for h in range(j + 3, 10):
                    if (sum_3m[i] + sum_3m[j] + sum_3m[h] - mm3 * 3) > save_m:
                        save_m = (sum_3m[i] + sum_3m[j] + sum_3m[h] - mm3 * 3)

        # 3달짜리가 4개일때
        if sum(final_plan) - mm3*4 > save_m:
            save_m = sum(final_plan) - mm3*4

        result -= save_m
        if result < ym:
            print(f'#{tc} {result}')
        else:
            result = ym
            print(f'#{tc} {result}')


# 가능한 모든 가격의 경우를 비교한 풀이
# DFS로 풀어 볼 것것