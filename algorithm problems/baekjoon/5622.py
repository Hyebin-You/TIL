word = input()
result = 0
alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MON', 'PQRS', 'TUV', 'WXYZ']

for char in word:
    for i in range(len(alpha)):
        if char in alpha[i]:
            result += i + 3

print(result)