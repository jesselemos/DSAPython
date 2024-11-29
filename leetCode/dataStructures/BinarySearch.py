"""
Binary Search
The Binary Search algorithm searches through an array and returns the index of the value it searches for.

Binary Search is much faster than Linear Search, but requires a sorted array to work.

The Binary Search algorithm works by checking the value in the center of the array. If the target value is lower, the next value to check is in the center of the left half of the array. This way of searching means that the search area is always half of the previous search area, and this is why the Binary Search algorithm is so fast.

This process of halving the search area happens until the target value is found, or until the search area of the array is empty.

Note: When writing time complexity using Big O notation we could also just have written O(logn), but O(log2n)
reminds us that the array search area is halved for every new comparison, which is the basic concept of 
Binary Search, so we will just keep the base 2 indication in this case.
O(log2n)
"""
def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

if result != -1:
    print("Value",myTarget,"found at index", result)
else:
    print("Target not found in array.")