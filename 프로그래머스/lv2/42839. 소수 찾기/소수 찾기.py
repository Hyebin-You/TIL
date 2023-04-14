from itertools import permutations


def isPrime(num):

    for i in range(2, int(num ** (1/2)) + 1):
        if not num % i:
            return False
    
    return True
    
    

def solution(numbers):
    answer = []
    numbers = list(numbers)
    for l in range(1, len(numbers) + 1):
        comb = permutations(range(len(numbers)), l)
        for c in comb:
            num = ''
            for k in c:
                num += numbers[k]
            num = int(num)
            if num <= 1:
                continue
            if num not in answer and isPrime(num):
                answer.append(num)   
    
    return len(answer)