def cal(pre, post, op):
    if op == '+':
        return int(pre) + int(post)
    elif op == '-':
        return int(pre) - int(post)
    else:
        return int(pre) * int(post)


N = int(input())
sentence = list(input())

result = -2 ** 31 - 1
q = [(sentence, [])]
while q:
    line, p = q.pop()
    if len(line) == 1:
        p += [int(line[0])]
        n = len(p)
        for _ in range(n//2):
            w = cal(p[0], p[2], p[1])
            p = [w] + p[3:]
        result = max(result, p[0])
        continue
    w = cal(line[0], line[2], line[1])
    if len(line) == 3:
        q.append(([w], p))
        q.append((line[2:], p + line[:2]))
    else:
        q.append((line[4:], p + [w] + [line[3]]))
        q.append((line[2:], p + line[:2]))

print(result)

# 이 문제는 pypy보다 python이 더 빠르게 나옴
# result 초기값 설정 주의할 것!