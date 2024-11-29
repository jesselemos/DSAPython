# print(0)
# print(1)
# count = 2

# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newFibo = prev1 + prev2
#         print(newFibo)
#         prev2 = prev1
#         prev1 = newFibo
#         count += 1
#         fibonacci(prev1, prev2)
#     else:
#         return

# fibonacci(1,0)

#my solution
# list = [x for x in range(0,20)]

# for i in range(0,len(list)):
#     if i > 1:
#         list[i] = list[i-1] + list[i-2]
# print(list)

#https://www.w3schools.com/dsa/dsa_algo_simple.php
# def F(n):
#     if n <= 1:
#         return n
#     else:
#         return F(n - 1) + F(n - 2)

# print(F(19))

#https://www.simplilearn.com/tutorials/python-tutorial/fibonacci-series#:~:text=The%20simplest%20way%20to%20print,recursively%20to%20generate%20the%20sequence.
# a, b, c = 0, 1, 0
# n = 20
# print(a)
# while c < n:
#     print(b)
#     a, b, c = b, a+b, c+1

def fibonnaci(num):
   if num < 0:
      raise Exception("number needs to be gt -1")
   fib = [0]
   prev, curr = 0, 1

   for i in range(num):
      fib.append(curr)
      curr, prev = curr + prev, curr
   print(fib)
   return fib

fibonnaci(20)
fibonnaci(0)
fibonnaci(-1)

