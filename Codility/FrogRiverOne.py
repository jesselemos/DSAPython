
"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""




"""
To solve the problem efficiently, we need to determine the earliest time when the frog can cross the river, which happens when all positions from 1 to X have leaves. The leaves fall in sequence, and their positions are given in the array A. The frog can cross once every position from 1 to X is covered by at least one leaf.

Approach:
Track Covered Positions: We need to keep track of the positions from 1 to X that have leaves. Using a set is ideal for this, as sets allow efficient lookups and inserts.

Earliest Time: Iterate through the array A, and for each leaf that falls, add its position to a set of covered positions. The goal is to find the earliest time when the set contains all the positions from 1 to X.

Edge Case: If the frog can't jump to the other side (i.e., not all positions from 1 to X are covered), we should return -1.

Steps in the Algorithm:
Initialize a set to store the positions covered by leaves.
Loop through the array A, adding the positions to the set.
If the set size reaches X (i.e., all positions 1 to X are covered), return the current time (index).
If after processing all leaves, the set doesn't contain all positions, return -1.
Python Code:
python
Copy code
def solution(X, A):
    covered_positions = set()  # to track the positions covered by leaves
    for time, position in enumerate(A):
        if position <= X:
            covered_positions.add(position)
        if len(covered_positions) == X:
            return time  # return the earliest time when all positions are covered
    return -1  # return -1 if not all positions are covered
Explanation:
Step 1: We initialize a set covered_positions to keep track of the positions that have leaves.
Step 2: We iterate through the array A using enumerate, which gives both the time (time) and the position (position) of the leaf falling at that time.
Step 3: If the position of the leaf is within the range [1, X], we add it to the set.
Step 4: As soon as the set has all the positions (i.e., its size reaches X), we return the current time (time), which is the earliest moment the frog can jump.
Step 5: If the loop finishes without covering all positions, return -1.
Example:
Given:

X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
The algorithm will work as follows:

At time 6, position 5 is covered, and all positions [1, 2, 3, 4, 5] are covered by leaves. Hence, the frog can jump at time 6.
Time Complexity:
The time complexity is O(N), where N is the length of the array A. This is because we are iterating through the array once and performing constant-time operations (set insertions and size checks) at each step.
Space Complexity:
The space complexity is O(X), where X is the maximum position the leaves can fall at, since the set can store up to X positions.
This solution is efficient enough to handle the problem constraints where N and X can go up to 100,000.
"""