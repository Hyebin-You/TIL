import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    pipes = input()
    pipe = 0
    result = 0

    for i in range(len(pipes)):
        if pipes[i] == '(':
            pipe += 1
        elif pipes[i] == ')' and pipes[i-1] == '(':
            pipe -= 1
            result += pipe
        else:
            pipe -= 1
            result += 1

    print(f'#{tc} {result}')