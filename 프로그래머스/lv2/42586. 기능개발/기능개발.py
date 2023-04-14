from collections import deque


def solution(progresses, speeds):
    answer = []
    prog = deque(progresses)
    sp = deque(speeds)
    
    while prog:
        l = len(prog)
        for i in range(l):
            prog[i] += sp[i]
        
        t = 0
        for i in range(l):
            if prog[i] >= 100:
                t += 1
            else:
                break
                
        if t:
            for _ in range(t):
                prog.popleft()
                sp.popleft()
            answer.append(t)
        
    
    
    
    return answer