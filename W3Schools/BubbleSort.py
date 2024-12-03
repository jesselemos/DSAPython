"""
Bubble Sort
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

How it works:
Go through the array, one value at a time.
For each value, compare the value with the next value.
If the value is higher than the next one, swap the values so that the highest value comes last.
Go through the array as many times as there are values in the array.

O(n2)
"""
arr = [5454, 55454, 878184,1548,1814,187184,197194,99,187184,1871]
n = len(arr)
for i in range(n-1):
   swapped = False
   for x in range(n-i-1):
      if arr[x+1] < arr[x]:
         arr[x], arr[x+1] = arr[x+1], arr[x]
         swapped = True
   if not swapped:
      break
print(arr)

