import sys

sys.stdin = open('input.txt')

for i in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0

    for j in range(2, n-2):
        # 양 옆 4개중 제일 높은 건물 높이 구하기
        heights = [arr[j-1], arr[j+1], arr[j+2]]
        max_h = arr[j-2]
        for h in heights:
            if max_h < h:
                max_h = h

        # 조망권을 구하고 싶은 건물과 주변의 제일 높은 건물 높이의 차를 결과에 더함
        if arr[j] > max_h:
            count += arr[j] - max_h

    print(f'#{i + 1} {count}')