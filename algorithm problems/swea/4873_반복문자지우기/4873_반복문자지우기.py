import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    words = input()
    result = []

    for i in range(len(words)):
        if len(result) == 0:
            result.append(words[i])
        else:
            prev = result.pop()
            if prev != words[i]:
                result.append(prev)
                result.append(words[i])

    print(f'#{tc} {len(result)}')