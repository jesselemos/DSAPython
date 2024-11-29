def slow_solution(n): 
    result = 0 
    for i in range(n): 
        for j in range(i + 1): 
            result += 1 
    return result
        
print(slow_solution(3))


def fast_solution(n): 
    result = 0 
    for i in range(n):
        result += (i + 1) 
    return result
        
print(fast_solution(3))


def model_solution(n): 
    result = result = n * (n + 1) // 2
    return result
        
print(model_solution(3))