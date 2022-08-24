import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))

    a = True
    while a:
        for i in range(1, 6):
            num = arr.pop(0)
            if num - i > 0:
                arr.append(num - i)
            else:
                arr.append(0)
                a = False
                break

    print(f'#{tc}', *arr)