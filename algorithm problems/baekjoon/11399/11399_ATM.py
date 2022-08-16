N = int(input())
arr = list(map(int, input().split())) # 입력 받아옴

arr.sort()  #입력받은 시간 오름차순 정렬
sums = 0

# 첫번째 시간은 첫번째 시간만, 두번째는 첫번째와 자기 자신을 더한 만큼 이므로
# 최종 결과인 sums에 처음부터 자기자신까지의 합을 더해줌
for i in range(N):
    sums += sum(arr[:i+1])

# 시간을 작은 순으로 나열하여 시간의 합을 구하는 것이 가장 작게 나온다.

print(sums)