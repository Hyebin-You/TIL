num = int(input())

i = 666
count = 1

while True:
    if '666' in str(i):
        if num == count:
            break
        else:
            i += 1
            count += 1
    else:
        i += 1
    

print(i)