import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda i: i[0]) #회의 시작 시간으로 정렬
arr.sort(key=lambda i: i[1]) #회의가 끝나는 시간으로 정렬
#두 정렬 순서가 반대가 되면 정답이 출력되지 않음

last = arr[0]  #정렬된 값들 중 제일 앞의 값을 변수에 할당
result = 1  # 제일 첫 값으로 비교하기 때문에 첫 값을 미리 결과에 넣어줌
for i in range(1, N): # 두번째 값부터 끝까지
    if arr[i][0] >= last[1]:
        #회의 시작시간이 이전에 마지막으로한 회의의 종료시간보다 같거나 크다면
        result += 1
        last = arr[i]   #마지막 회의 갱신

print(result)