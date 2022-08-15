total_round, a, b = map(int, input().split())
result = 0

while True:   
    if abs(a - b) == 1 and min(a,b) % 2 == 1:
        result += 1
        break
    else:
        result += 1

    if a % 2:
        a = (a + 1) // 2
    else:
        a = a // 2
    
    if b % 2:
        b = (b + 1) // 2
    else:
        b = b // 2

print(result)

# 여기는 라운드가 진행될 때마다 a와 b의 번호가 갱신되는 방법