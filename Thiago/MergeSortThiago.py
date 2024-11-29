

def printArray():
   arr = []
   for i in range(10):
      arr.append(i)
   return arr

print(printArray())



# from typing import List

# array = [4,3,2,1]

# def mergeSort(array: List):
#    if len(array) <= 1:
#       return array
   
#    mid = len(array) // 2

#    leftArray = array[:mid]
#    rightArray = array[mid:]

#    # print(f"leftArray={leftArray}")
#    # print(f"rightArray={rightArray}")

#    left = mergeSort(leftArray)
#    right = mergeSort(rightArray)

#    # print(f"left={left}")
#    # print(f"right={right}")

#    ret = merge(left, right)
#    print(f"mergeSort.ret{ret}")
#    return ret

# def merge(left: List, right: List):
#    arrayRet = []
#    print(f"arrayRet={arrayRet} left={left} right{right}")
#    # if len(arrayRet) == 4:
#    #    return arrayRet
#    for i in left:
#       for j in right:
#          print(f"i={i} j={j}")
#          if i < j:
#             arrayRet.append(i)
#          else:
#             arrayRet.append(j)

#    arrayRet += arrayRet
#    return arrayRet

# sorted = mergeSort(array)
# print(f"sorted{sorted}")


