# A = [1,1,1,1,5,5,5,0,8,1,1,1,1,1]
# m = 100

# def counting(A, m): 
#     n = len(A) 
#     count = [0] * (m + 1) 
#     for k in range(n): 
#         count[A[k]] += 1 
#     return count

# print(counting(A,m))


def rec(n):
   print("start", n)
   if(n <= 0 ):
    return 0
   print("pre", n)
   n = rec(n - 1)
   print("post", n)
   return n

rec(2)