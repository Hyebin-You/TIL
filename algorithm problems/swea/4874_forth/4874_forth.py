import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input().split()
    num = []

    result = 0
    for i in range(len(word)):
        if word[i] in '+-*/':
            if len(num) < 2:
                result = 'error'
            else:
                a = num.pop()
                b = num.pop()
                if word[i] == '+':
                    num.append(a+b)
                elif word[i] == '-':
                    num.append(b-a)
                elif word[i] == '*':
                    num.append(a*b)
                else:
                    num.append(b//a)
        elif word[i] == '.':
            if result == 'error':
                print(f'#{tc} {result}')
            else:
                if len(num) != 1:
                    print(f'#{tc} error')
                else:
                    print(f'#{tc} {num[0]}')
        else:
            num.append(int(word[i]))