import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = input()
    dict_alpha = {}
    for i in range(len(str1)):
        dict_alpha[str1[i]] = 0

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                dict_alpha[str1[i]] += 1

    max_num = dict_alpha[str1[0]]
    for k in dict_alpha:
        if max_num < dict_alpha[k]:
            max_num = dict_alpha[k]

    print(f'#{tc} {max_num}')