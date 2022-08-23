import sys
sys.stdin = open('test_input.txt', encoding='utf-8')


def bruteForce(pattern, target):
    # 현재 조사 대상인 각 idx 초기화
    p_idx, t_idx = 0, 0
    # 패턴이 몇번 나오느냐
    count = 0
    while t_idx < len(target):
        # 조사 대상을 변수에 담아서 사용
        t = target[t_idx]
        p = pattern[p_idx]

        #두 값이 서로 다를때
        if t != p:
            t_idx -= p_idx
            p_idx = -1

        t_idx += 1
        p_idx += 1

        # 만약 모든 패턴 조사가 다 끝났다면
        if p_idx == len(pattern):
            count += 1
            p_idx = 0

    return count


def bruteForce_for(pattern, target):
    count = 0
    for i in range(len(target) - len(pattern) + 1):
        for j in range(len(pattern)):
            # 두 값이 다른 경우가 나올때 까지
            if pattern[j] != target[i+j]:
                break
        else:
            count += 1
    return count


for _ in range(10):
    tc = input()
    f_word = input()
    sentence = input()
    result = 0

    for i in range(len(sentence)-len(f_word)+1):
        for j in range(len(f_word)):
            if sentence[i + j] != f_word[j]:
                break
        else:
            result += 1

    print(f'#{tc} {result}')

    j = 0
    result1 = 0
    while j <= len(sentence)-len(f_word):
        for i in range(len(f_word)):
            if sentence[i+j] != f_word[i]:
                break
        else:
            result1 += 1
        j += 1

    print(result1)

    #내장 메서드 있음
    print(bruteForce(f_word, sentence))