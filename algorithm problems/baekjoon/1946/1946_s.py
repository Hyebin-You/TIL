import sys
input=sys.stdin.readline

T = int(input())

for tc in range(T):   # 테스트 케이스 개수만큼 순회
    N = int(input())
    #지원자 성적 리스트로 받아옴
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    
    arr.sort() # 서류심사 성적으로 오름차순 정렬
    min_n = arr[0][1] # 제일 작은 값을 첫번째 사람의 면접 성적으로 두고
    for j in range(N): # 전체 지원자들 순회
        if arr[j][1] <= min_n:  # 현재 지원자의 면접성적이 더 낮으면(즉 순위가 높으면)
            count += 1
            # 같은 경우도 더해주는 이유는 제일 처음의 count를 0으로 놓았기 때문에
            # 첫번째 지원자를 뽑기 위해서
            min_n = arr[j][1] # 제일 작은 면접 성적 갱신

    print(count)

#얘는 위에 input 바꾸니까 성공