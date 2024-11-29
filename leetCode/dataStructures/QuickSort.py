"""
Quicksort
As the name suggests, Quicksort is one of the fastest sorting algorithms.

The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.

Speed: 

New Values Done!
In this tutorial the last element of the array is chosen to be the pivot element, but we could also have chosen the first element of the array, or any element in the array really.

Then, the Quicksort algorithm does the same operation recursively on the sub-arrays to the left and right side of the pivot element. This continues until the array is sorted.

Recursion is when a function calls itself.

After the Quicksort algorithm has put the pivot element in between a sub-array with lower values on the left side, and a sub-array with higher values on the right side, the algorithm calls itself twice, so that Quicksort runs again for the sub-array on the left side, and for the sub-array on the right side. The Quicksort algorithm continues to call itself until the sub-arrays are too small to be sorted.

The algorithm can be described like this:

How it works:

Choose a value in the array to be the pivot element.
Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

The worst case scenario for Quicksort is O(n2)
But on average, the time complexity for Quicksort is actually just 
O(n log n)
"""

"""
Youtube FelixTechTips Version
https://www.youtube.com/watch?v=9KBwdDEwal8&t=289s
"""
# arr = [3, 6, 8, 10, 1, 2]
# def quicksort(arr,left,right):
#    if left < right:
#       pivot_pos = partition(arr,left,right)
#       quicksort(arr, left, pivot_pos - 1)
#       quicksort(arr, pivot_pos + 1, right)

# def partition(arr,left,right):
#    i = left
#    j = right -1
#    pivot = arr[right]
#    while i < j:
#       while i < right and arr[i] < pivot:
#          i +=1
#       while j > left and arr[j] >= pivot:
#          j -=1
      
#       if i < j:
#          arr[i], arr[j] = arr[j], arr[i]
      
#       if arr[i > pivot]:
#          arr[i], arr[right] = arr[right], arr[i]

#       return i
# quicksort(arr,0,len(arr)-1)
# print(arr)





"""
W3Schools Version
https://www.w3schools.com/dsa/dsa_algo_quicksort.php
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [2,1,4,3]
quicksort(my_array)
print("Sorted array:", my_array)
"""


"""
Chat GPT Version:
def quicksort(arr):
   #  Perform Quicksort on a list.

   #  Parameters:
   #  arr (list): The list to be sorted.

   #  Returns:
   #  list: A new sorted list.

    # Base case: if the array is of length 0 or 1, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (using the middle element as an example)
    pivot = arr[len(arr) // 2]

    # Partition the array into three parts
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort the left and right parts, and concatenate the results
    return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print("Original:", arr)
print("Sorted:", sorted_arr)
"""
def quicksort(arr):
    if len(arr) <= 1: # Base case: if the array is of length 0 or 1, it's already sorted
        return arr

    pivot = arr[len(arr) // 2] # Choose a pivot (using the middle element as an example)

    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quicksort(left) + middle + quicksort(right) # Recursively sort the left and right parts, and concatenate the results

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print("Original:", arr)
print("Sorted:", sorted_arr)