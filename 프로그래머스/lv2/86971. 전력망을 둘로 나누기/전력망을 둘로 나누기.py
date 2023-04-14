def get_num(s1, s2, n, ar):
    stack = [s1]
    visited = [0] * n
    
    while stack:
        s = stack.pop()
        if not visited[s - 1]:
            visited[s-1] = 1
            for i in ar[s]:
                if i != s2:
                    stack.append(i)
                    
    return visited.count(1)


def solution(n, wires):
    answer = n
    info = {k: [] for k in range(1, n + 1)}
    
    for w in wires:
        info[w[0]].append(w[1])
        info[w[1]].append(w[0])
    
    for w in wires:
        s1, s2 = w
        cnt1, cnt2 = get_num(s1, s2, n, info), get_num(s2, s1, n, info)
        answer = min(answer, abs(cnt1 - cnt2))
            
    return answer