import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    i = 0
    counts = 0
    while True:
        if B[0] != A[i]: #문자열의 i번째가 패턴의 시작점과 같지 않다면 i 1 증가
            i += 1
        else: # 패턴의 시작점과 같다면
            for j in range(1, len(B)): # 그 이후부터 패턴의 끝까지 순회
                if A[i+j] != B[j]: #만약 패턴 중간에 다른 부분이 있다면
                    i += 1   #i를 1 증가시키고
                    break #패턴과 맞는지 탐색하는 반복문 종료
            else: # 패턴 끝까지 순회 후 다른 부분이 없다면(패턴과 일치한다면)
                counts += 1  #패턴 등장 수를 1 증가시키고
                i += len(B) #패턴길이 이후로 i를 이동

        if i > len(A) - len(B):  #i부터 문자열 끝까지의 길이가 패턴 길이보다 짧다면
            break  #더 이상 패턴이 존재할 수 없으므로 while문 종료

    #최종 타이핑 횟수는 패턴 등장 수에 패턴이 아닌 문자들의 수를 더한 것
    result = counts + (len(A) - len(B) * counts)
    print(f'#{tc} {result}')