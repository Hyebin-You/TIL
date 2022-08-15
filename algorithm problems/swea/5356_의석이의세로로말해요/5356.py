import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    result = ''

    max_l = len(arr[0])
    for words in arr:
        if len(words) > max_l:
            max_l = len(words)

    for j in range(max_l):
        for words in arr:
            if j < len(words):
                result += words[j]

    print(f'#{tc} {result}')