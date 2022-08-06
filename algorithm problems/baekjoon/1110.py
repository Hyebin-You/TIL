result = 0
first_num = int(input())
num = first_num

while True:
    if num < 10:
        new_num = str(num)*2
    else:
        new_num = str(num % 10) + str((num // 10 + num % 10) % 10)
    
    result += 1
    if first_num == int(new_num):
        print(result)
        break

    num = int(new_num)