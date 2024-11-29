"""
Example: Weare given some positive integer n. 
Let’s compute the factorial of n and assign it to the variable factorial. 
The factorial of n is n! = 1 · 2 · ... · n. 
We can obtain it by starting with 1 and multiplying it by all the integers 
from 1 to n. 
"""
import math

n=5
def factorial_iterative(n):
   factorial = 1
   for i in range (1, n + 1):
      factorial *= i
   return factorial

def factorial_recursive(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial_recursive(n - 1)

print(f"factorial_iterative(n): {factorial_iterative(n)}")
print(f"factorial_recursive(n): {factorial_recursive(n)}")
print(f"math.factorial(n): {math.factorial(n)}") 