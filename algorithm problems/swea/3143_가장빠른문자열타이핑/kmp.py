import sys
sys.stdin = open('sample_input.txt')


def make_failure_function(p):

    failure_function = [0] * (len(p))
    counter = 0

    for idx in range(1, len(p)):
        while counter > 0 and p[counter] != p[idx]:
            counter = failure_function[counter-1]
        if p[counter] == p[idx]:
            counter += 1
            failure_function[idx] = counter
    return failure_function


def kmp_matching(s, p, p_table):
    counter = 0
    idx = 0
    fin_idx = len(s)
    cnt = 0
    while idx < fin_idx:
        while counter > 0 and s[idx] != p[counter]:
            counter = p_table[counter-1]
        if s[idx] == p[counter]:
            if counter == len(p) - 1:
                cnt += 1
                counter = 0
            else:
                counter += 1
        idx += 1
    return cnt


def fast_typing(st, pa):
    failure_table = make_failure_function(pa)
    pattern_matching_cnt = kmp_matching(st, pa, failure_table)
    answer = len(st) - pattern_matching_cnt*(len(pa)-1)
    return answer


for test in range(1, int(input())+1):
    string, pa = input().split()
    print(f'#{test} {fast_typing(string, pa)}')