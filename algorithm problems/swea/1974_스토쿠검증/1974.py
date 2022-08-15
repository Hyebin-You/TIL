import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 행,열 확인
    for i in range(9):
        nums_row = set()
        nums_col = set()
        for j in range(9):
            nums_row.add(arr[i][j])
            nums_col.add(arr[j][i])
        if len(nums_col) != 9 or len(nums_row) != 9:
            result = 0

    # 작은 정사각형 확인
    for k in range(0, 9, 3):
        for h in range(0, 9, 3):
            nums = set()
            for i in range(3):
                for j in range(3):
                    nums.add(arr[k+i][h+j])
            if len(nums) != 9:
                result = 0

    print(f'#{tc} {result}')