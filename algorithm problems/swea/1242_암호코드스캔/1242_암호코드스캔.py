import sys
sys.stdin = open('sample_input.txt')


def sixteentotwo(nums):
    num_dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
               '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
               'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    n_c = ''

    for num in nums:
        n_c += num_dic[num]

    for i in range(len(n_c)-1, 0, -1):
        if n_c[i] == '1':
            n_c = n_c[:i+1]
            break

    return n_c


def find_width(num_code):
    i = 1
    a, b, c = 0, 0, 0
    while True:
        if num_code[-i] == '1':
            if not b:
                a += 1
                i += 1
            else:
                c += 1
                i += 1
        else:
            if not c:
                b += 1
                i += 1
            else:
                break
    return min(a, b, c)


def decode(num_code, w):
    global final_result
    decode_num = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
                  '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
                  '0110111': 8, '0001011': 9}

    result = [0] * 9
    k = len(num_code) - 56 * w
    code1 = num_code[k:]
    other = num_code[:k]

    word = ''
    idx = 1
    for i in range(0, len(code1), w):
        word += code1[i]
        if word in decode_num.keys():
            result[idx] = decode_num[word]
            word = ''
            idx += 1

    num_odd = result[1] + result[3] + result[5] + result[7]
    num_even = result[2] + result[4] + result[6]
    if not (num_odd * 3 + num_even + result[8]) % 10:
        if result not in final_result:
            final_result.append(result)

    if len(other) == other.count('0'):
        return
    else:
        for i in range(len(other) - 1, 0, -1):
            if other[i] == '1':
                other = other[:i + 1]
                break
        w_1 = find_width(other)
        decode(other, w_1)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    code_arr = []
    for _ in range(N):
        line = input().strip()
        if line not in code_arr and len(line) != line.count('0'):
            code_arr.append(line)

    final_result = []
    for code in code_arr:
        code = sixteentotwo(code)
        w = find_width(code)
        decode(code, w)

    total = 0
    for i in range(len(final_result)):
        for j in range(1, 9):
            total += final_result[i][j]

    print(f'#{tc} {total}')