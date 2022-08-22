sentence = input().split('-')  # - 를 기준으로 끊어서 받음
result = 0

for i in range(len(sentence)):
    subset = sentence[i].split('+')  # 그 뒤 + 로 끊어서
    subset_sum = 0
    for j in subset:   # + 앞뒤로 있던 숫자들의 합을 구함
        subset_sum += int(j)
    if i == 0:  # 제일 처음 숫자는 result에 더하고
        result += subset_sum
    else:       # 그 뒤에 오는 숫자들은 모두 빼줌
        result -= subset_sum

print(result)