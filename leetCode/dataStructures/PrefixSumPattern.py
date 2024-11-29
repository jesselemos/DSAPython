"""
https://www.youtube.com/watch?v=DjYZk8nrXVY
https://blog.algomaster.io/p/15-leetcode-patterns

Prefix Sum involves preprocessing an array to create a new array where each element at index i represents the sum of the array from the start up to i. This allows for efficient sum queries on subarrays.

Use this pattern when you need to perform multiple sum queries on a subarray or need to calculate cumulative sums.

Sample Problem:
Given an array nums, answer multiple queries about the sum of elements within a specific range [i, j].

Example:
Input: nums = [1, 2, 3, 4, 5, 6], i = 1, j = 3
Output: 9

Explanation:
Preprocess the array A to create a prefix sum array: P = [1, 3, 6, 10, 15, 21].

To find the sum between indices i and j, use the formula: P[j] - P[i-1].
Leet Codes 303,525,560
303: https://leetcode.com/problems/range-sum-query-immutable/
525: https://leetcode.com/problems/contiguous-array/description/
560: https://leetcode.com/problems/subarray-sum-equals-k/
"""


#Simple way (O n*m)
from typing import List


array = [1, 2, 3, 4, 5, 6]

def find_subarray_sum(array, i, j):
    sum = 0
    for k in range(i,j+1):
        sum += array[k]
    return sum

#print(find_subarray_sum(array, 1,3))

"""
Pattern way
"""
def create_prefix_sum(arr):
    for i in range(1, len(array)):
        arr[i] += arr[i-1]
    return arr

newArray = create_prefix_sum(array)

def find_newarray_sum(i,j):
    return newArray[j] - newArray[i-1]

#print(find_newarray_sum(1,3))



"""
303. Range Sum Query - Immutable
Solved
Easy
Topics
Companies
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Solution 1: Runtime 2314ms Beats 6.46%
"""
class NumArray:
    nums = []
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        val = 0
        for k in range(left, right+1):
            val += self.nums[k]
        return val

numArray = NumArray([-2, 0, 3, -5, 2, -1])
result = numArray.sum_range(0, 2) # return (-2) + 0 + 3 = 1

#print(result)


"""
303. Range Sum Query - Immutable

Solution 2: 703ms Beats 24.62%
"""
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
    

"""
https://leetcode.com/problems/contiguous-array/

525. Contiguous Array
Solved
Medium
Topics
Companies
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

Test Cases:
[0,1,0,1,0,1,0,1,0,1]
[0,1,0,1,1,1,1,1,1,1,1,1,1,1]
[0,0,0,1,1,1,0]
[1,1,1,1,0,0,0,0,1,0,1,0,1]
[1,1,1,1,0]
"""

class Solution(object):
    def findMaxLength(self, nums):
        counter = 0
        max_len = 0
        dic = {0:0}

        for i, num in enumerate(nums,1):
            if num == 0:
                counter -=1
            else:
                counter+=1
            
            if counter in dic:
                max_len = max(max_len, i - dic[counter])
            else:
                dic[counter] = i

        return max_len

print(Solution().findMaxLength([0,1,1,1,1]))


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mx=0
        count=0
        countToIndex = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 1 : 
                count +=1
            else: 
                count -=1

            if count in countToIndex:
                mx=max(mx, i-countToIndex[count])
            else:
                countToIndex[count] = i
                
        return mx 
    
print(Solution().findMaxLength([0,1,1,1,1]))