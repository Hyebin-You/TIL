import sys
sys.stdin = open('sample_input.txt')


def find_tri(arr):
    for i in range(8):
        if arr[i] and arr[i+1] and arr[i+2]:
            return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10

    for i in range(12):
        if not i % 2:
            n = nums[i]
            p1[n] += 1
            if p1.count(3) or find_tri(p1):
                print(f'#{tc} {1}')
                break
        else:
            n = nums[i]
            p2[n] += 1
            if p2.count(3) or find_tri(p2):
                print(f'#{tc} {2}')
                break
    else:
        print(f'#{tc} {0}')