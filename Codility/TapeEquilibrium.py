"""
TapeEquilibrium
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""
#My Solution
A = [5, -2, 3]
def solution(A):
    total = diff = sum(A)
    left = 0
    diff = float('inf')
    for i in range(len(A)-1):
        left += A[i]
        right = total - left
        diff = abs(left - right)
        min_diff = min(min_diff, diff)
    return min_diff

print(solution(A))

#ChatGPT Solution
def solution2(A):
    total_sum = sum(A)  # Calculate the total sum of the array
    left_sum = 0
    min_difference = float('inf')  # Start with a very large value
    print(f"min_difference={min_difference}")
    for i in range(len(A) - 1):  # Iterate until the second-to-last element
        left_sum += A[i]  # Add the current element to the left part
        right_sum = total_sum - left_sum  # Calculate the right part dynamically
        difference = abs(left_sum - right_sum)  # Compute the absolute difference
        min_difference = min(min_difference, difference)  # Update the minimum difference
        print(f"left_sum={left_sum} right_sum={right_sum} difference={difference} min_difference={min_difference}")
    return min_difference

print(solution2(A))


