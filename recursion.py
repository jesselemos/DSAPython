def rec(n):
   if(n >= 5 ):
      print("basecase", n)
      return -1
   print("pre", n)
   n = rec(n + 1)
   print("post", n)
   return n
rec(0)

"""
stack = by Value - fast
heap = by reference - slow
"""