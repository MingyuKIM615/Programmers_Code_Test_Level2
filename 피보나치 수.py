def solution(n):
    answer = 0
    p = []
    for i in range(n+1):
        if i == 0:
            p.append(0)
        elif i == 1:
            p.append(1)
        else:
            p.append(p[i-1] + p[i-2])
            
    answer = p[-1] % 1234567
            
    
    return answer
