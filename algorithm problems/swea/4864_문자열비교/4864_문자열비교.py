import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    for i in range(len(str2)-len(str1)+1):
        counts = 0
        for j in range(len(str1)):
            if str2[i+j] == str1[j]:
                counts += 1
        if counts == len(str1):
            result = 1
            break
    else:
        result = 0

    print(f'#{tc} {result}')

    #브루트 포스로 해결. 다른 방식도 시도해보기