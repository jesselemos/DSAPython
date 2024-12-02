def solution(A):
    diff = 0
    for i in range(len(A)):
        if diff == 0:
            diff = abs(sum(A[i:]) - sum(A[:i]))
        else: 
            diff = min(diff,abs(sum(A[i:]) - sum(A[:i])))
    return diff

