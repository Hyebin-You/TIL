def solution(brown, yellow):
    answer = []
    area = brown + yellow
    for i in range(3, int(area **(1/2)) + 1):
        if not area % i:
            b = i
            a = area // i
            if 2 * (a + b) - 4 == brown and (a - 2) * (b - 2) == yellow:
                answer = [a, b]
    
    return answer