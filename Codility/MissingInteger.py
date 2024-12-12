"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution(A):
    # Filter and keep only positive numbers, then convert to a set for O(1) lookups
    positive_numbers = set(num for num in A if num > 0)
    
    # Start checking from 1 upwards
    smallest_missing = 1
    while smallest_missing in positive_numbers:
        smallest_missing += 1
    
    return smallest_missing
