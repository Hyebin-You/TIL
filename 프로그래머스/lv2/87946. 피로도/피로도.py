from itertools import permutations


def solution(k, dungeons):
    answer = -1
    l = len(dungeons)
    pp = permutations(range(l), l)
    for p in pp:
        tired = k
        cnt = 0
        for i in range(l):
            idx = p[i]
            if dungeons[idx][0] <= tired:
                cnt += 1
                tired -= dungeons[idx][1]
            else:
                break
        answer = max(answer, cnt)
    
    return answer