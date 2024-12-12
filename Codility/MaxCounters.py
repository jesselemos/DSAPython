"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].


ChatGPT Answer:
To efficiently solve the problem, we can implement the function to handle the operations on the counters without incurring unnecessary overhead from updating all counters during a "max counter" operation. Here's the implementation:

Optimized Algorithm
Instead of updating all counters during a max counter operation, we keep track of:

max_value: The maximum value of any counter at any time.
current_min: The "lazy update" value representing the minimum value to which all counters should be updated.
Steps:
Initialize all counters to 0.
For each operation in A:
If it's an increase(X) operation (1 ≤ X ≤ N), update counter X directly, ensuring it is at least current_min.
If it's a max counter operation (A[K] = N + 1), set current_min to max_value.
After processing all operations, ensure all counters are at least current_min.
"""

def solution(N, A):
    counters = [0] * N
    max_value = 0
    current_min = 0
    
    for operation in A:
        if 1 <= operation <= N:
            # Convert operation to zero-based index
            index = operation - 1
            # Lazy update: ensure counter is at least current_min
            if counters[index] < current_min:
                counters[index] = current_min
            # Increment counter
            counters[index] += 1
            # Update max_value if needed
            if counters[index] > max_value:
                max_value = counters[index]
        elif operation == N + 1:
            # Lazy update for max counter operation
            current_min = max_value
    
    # Final pass: Ensure all counters are at least current_min
    for i in range(N):
        if counters[i] < current_min:
            counters[i] = current_min
    
    return counters
