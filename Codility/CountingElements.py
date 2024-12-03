#Storing counting in another array
A = [1,1,1,1,5,5,5,0,8,1,1,1,1,9]
m = len(A)

def counting(A, m): 
    n = len(A) 
    count = [0] * (m + 1) 
    for k in range(n): 
        count[A[k]] += 1 
    return count

print(counting(A,m))


