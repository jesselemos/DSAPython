"""
OddOccurrencesInArray
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""

"""
My Solution 1 
▶ medium1
medium random test n=2,001✘ TIMEOUT ERROR
running time: 0.152 sec., time limit: 0.100 sec.
▶ medium2
medium random test n=100,003✘ TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶ big1
big random test n=999,999, multiple repetitions✘ TIMEOUT ERROR
Killed. Hard limit reached: 7.000 sec.
▶ big2
big random test n=999,999 ✘ TIMEOUT ERROR
Killed. Hard limit reached: 7.000 sec.

"""
# def solution(A):
#     i = 0
#     l = len(A)-1
#     while i <= l:
#         j = i
#         curr = A[i]
#         while curr > 0 and j <= l:
#             if i != j and curr == A[j]:
#                 A[i], A[j] = 0, 0
#                 break
#             if j == l:
#                 return curr
#             j += 1
#         i += 1
#     return curr

"""
My Solution 2 
▶medium1
medium random test n=2,001✘TIMEOUT ERROR
running time: 0.116 sec., time limit: 0.100 sec.
▶medium2
medium random test n=100,003✘TIMEOUT ERROR
Killed. Hard limit reached: 6.000 sec.
▶big1
big random test n=999,999, multiple repetitions✘TIMEOUT ERROR
Killed. Hard limit reached: 7.000 sec.
▶big2
big random test n=999,999✘TIMEOUT ERROR
Killed. Hard limit reached: 7.000 sec.

"""
# def solution(A):
#     i = 0
#     l = len(A)-1
#     while i <= l:
#         j = i + 1
#         curr = A[i]
#         alone = False if curr == 0 else True
#         while curr > 0 and j <= l:
#             if curr == A[j]:
#                 A[i], A[j] = 0, 0
#                 alone = False
#                 break
#             j += 1
#         if alone:
#            return curr
#         i += 1
#     return curr

import time
start_time = time.time()

# def solution(A):
#     i = 0
#     l = len(A)-1
#     while i <= l:
#         j = i + 1
#         curr = A[i]
#         while curr > 0 and j <= l:
#             if curr == A[j]:
#                 A[i], A[j] = 0, 0
#                 break
#             elif j == l:
#                 return curr
#             j += 1
#         i += 1
#     return curr

# def solution(A):
#     i = j = 0
#     l = len(A)-1
#     curr = A[i]
#     while curr > 0 and i <= l and j <= l:
#         j = i + 1
#         curr = A[i]
#         if A[i] == A[j]: 
#             A[i], A[j] = 0, 0
#             break
#         elif j == l:
#             return A[i]
#         j += 1
#         i += 1
#     return curr

#ChatGPT 1
# def solution(A):
#     result = 0
#     for number in A:
#         result ^= number  # XOR all the numbers
#     return result

#ChatGPT 2
def solution(A):
    counts = {}
    for number in A:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
    for key, value in counts.items():
        if value % 2 != 0:
            return key

ret = solution([9,3,9,3,9,7,9])
print(ret)

print("Process finished --- %s seconds ---" % (time.time() - start_time))

"""
#tests
[9,3,9,3,9,7,9]
[7]
[7,3,9,3,9,9,9]
[9,3,9,3,9,9,7]
[9,7,9,3,9,9,3]
[7,9,7,42,9,7,9,9,23,23,42]
"""

