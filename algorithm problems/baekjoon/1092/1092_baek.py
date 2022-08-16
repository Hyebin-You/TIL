import sys
input = sys.stdin.readline

N = int(input())
limit_weight = list(map(int, input().split()))

M = int(input())
box_weight = list(map(int, input().split()))

limit_weight.sort(reverse=True) # 크레인 무게제한과 상자 무게 내림차순 정렬
box_weight.sort(reverse=True)

result = 0
if box_weight[0] > limit_weight[0]: #크레인의 무게제한 중 가장 큰 값이
    print(-1)                       #가장 무거운 상자보다 작다면 -1 출력 후 종료
    sys.exit()

while len(box_weight) > 0: # 옮겨지지 않은 상자가 있는동안
    for i in range(len(limit_weight)):  #전체 크레인에 대해 순회
        for j in range(len(box_weight)):  #전체 박스에 대해 순회
            if limit_weight[i] >= box_weight[j]:  #크레인이 박스를 옮길 수 있다면
                del box_weight[j]   #해당 박스를 제거하고
                break      #박스에 대한 반복문 종료

    result += 1

print(result)

# 시간 초과... pypy로 하니 통과됨...