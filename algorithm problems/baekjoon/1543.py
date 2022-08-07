docu = input()
word = input()
result = 0

while True:
    if len(docu) < len(word):
        break

    count = 0
    for i in range(len(word)):
        if word[i] == docu[i]:
            count += 1
    
    if count == len(word):
        result += 1
        if len(word) == len(docu):
            break
        else:
            docu = docu[len(word):]
    else:
        docu = docu[1:]

print(result)