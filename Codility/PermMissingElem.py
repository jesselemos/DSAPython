""""
PermMissingElem
Find the missing element in a given permutation.

Task description
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

1 2 3 4      Sum = 10
1 2 3 4 5    Sum = 15
1 2 3 4 5 6  Sum = 21
"""

#my solution passed
#Detected time complexity:
#O(N) or O(N * log(N))
def solution(A):
    sum = 0
    expected = 1
    current = 2
    for i in range(len(A)):
        expected += current
        current+=1
        sum += A[i]
    return expected - sum

#chat GPT solution
"""
Complexity
Time Complexity: 𝑂(𝑁)O(N)
Calculating the sum of the array and the formula each take 
𝑂(𝑁)O(N).
Space Complexity: 𝑂(1)
O(1) Only a few variables are used for computation.
"""
def solution(A):
    N = len(A)
    total_sum = (N + 1) * (N + 2) // 2  # Expected sum from 1 to N+1
    actual_sum = sum(A)  # Sum of elements in the array
    return total_sum - actual_sum  # The missing number

