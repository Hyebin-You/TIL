N = int(input())
stack = []
nums = [int(input()) for _ in range(N)]

i = 1
idx = 0
result = []

while True:
    if idx == N:
        break

    if i <= N:
        if len(stack):
            if stack[-1] == nums[idx]:
                stack.pop()
                idx += 1
                result.append('-')
            else:
                stack.append(i)
                result.append('+')
                i += 1
        else:
            stack.append(i)
            result.append('+')
            i += 1
    else:
        if stack[-1] == nums[idx]:
            stack.pop()
            idx += 1
            result.append('-')
        else:
            result = ['NO']
            break

for l in result:
    print(l)