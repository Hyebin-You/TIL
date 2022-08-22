import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
arr = list(range(2, N+1))
num = 2
i = 1
remove_list = []   # 제거된 숫자들이 담길 리스트
while True:
    if num * i <= N:
        if num * i not in remove_list:  # 아직 제거되지 않았다면
            remove_list.append(num*i)   # 제거 리스트에 추가
            cnt += 1                    # 제거 카운트 증가
        i += 1
    else:                               # num 의 배수를 모두 제거했다면
        num += 1                        # num 증가
        i = 1

    if cnt == K:                        # 원하는 K와 카운트가 같다면 종료
        break

print(remove_list[-1])                  # 제거된 수들 중 제일 마지막 수 출력