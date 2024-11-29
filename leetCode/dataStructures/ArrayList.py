"""
Algorithm: Find The Lowest Value in an Array

How it works:
Go through the values in the array one by one.
Check if the current value is the lowest so far, and if it is, store it.
After looking at all the values, the stored value will be the lowest of all values in the array.

"""

# arr = [5454, 55454, 878184,1548,1814,187184,197194,99,187184,1871]

# low = arr[0]
# for x in arr:
#    if x < low: 
#      low = x
# print(low)


#Reverse an array
A = [1,2,3,4,5,6]
B = [1,2,3,4,5,6]
C = [1,2,3,4,5,6]
def reverse(A):
   N = len(A)
   for i in range(N//2):
     k = N - i - 1
     A[i], A[k] = A[k], A[i]
   return A
print(reverse(A))
print(list(reversed(B))) #Python built in function
print(C[::-1])



    
