def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        a = answers[i]
        if first[i % 5] == a:
            scores[0] += 1
        if second[i % 8] == a:
            scores[1] += 1
        if third[i % 10] == a:
            scores[2] += 1
    
    answer = []       
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i + 1)
    
    return answer