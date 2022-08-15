total_round, a, b = map(int, input().split())

i = 1
while True:
    if a // 2**i == b // 2 **i:
        if a % 2**i != 0 and b % 2**i != 0:
            break
    elif abs(a//2**i - b//2**i) == 1:
        if max(a,b) % 2**i == 0 and min(a,b) % 2**i != 0:
            break
    
    i += 1     

print(i)

# i번째 라운드에 맞붙는 수는 2**i 범위 내에 존재
# 어떤 i라운드에 숫자들이 존재하는지 확인하는 방법