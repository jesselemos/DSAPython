'''
3 -  40 mins
Simulate the Linux command to delete the entire tree directory:
Create a method that would simulate the Linux command: rm -R < folder >
Solution with better memory consuming 
Python preset code:
def list_directoy_items(path: str) -> list[str]:
  return ['..', '...']

# delete files, and folder if its empty
def del_item(path: str) -> None:
  pass

def is_directory(patth: str) -> bool:
  True

def my_solution(directoy_path: str) -> None:
# write your code here
'''

def list_directoy_items(path: str) -> list[str]:
    return ['..', '...']

# '''
# 1 -  20 mins
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some(can be none) of the characters without disturbing 
# the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
# '''

# def isSubsequence(s, t):
#     i = 0
#     j = 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#     return i == len(s)

# print(isSubsequence("ace", "abcde")) # True
# print(isSubsequence("aec", "abcde")) # False

# '''
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# '''
# def longestConsecutive(nums):
#     nums = set(nums)
#     longest = 0
#     for num in nums:
#         if num - 1 not in nums:
#             current_num = num
#             current_length = 1
#             while current_num + 1 in nums:
#                 current_num += 1
#                 current_length += 1
#             longest = max(longest, current_length)
#     return longest




# print(longestConsecutive([100,4,200,1,3,2])) # 4
   