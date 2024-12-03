#https://www.w3schools.com/dsa/dsa_theory_hashtables.php
"""
Hash Tables Summarized
Hash Table elements are stored in storage containers called buckets.

Every Hash Table element has a part that is unique that is called the key.

A hash function takes the key of an element to generate a hash code.

The hash code says what bucket the element belongs to, so now we can go directly to that Hash Table element: to modify it, or to delete it, or just to check if it exists. Specific hash functions are explained in detail on the next two pages.

A collision happens when two Hash Table elements have the same hash code, because that means they belong to the same bucket. A collision can be solved in two ways.

Chaining is the way collisions are solved in this tutorial, by using arrays or linked lists to allow more than one element in the same bucket.

Open Addressing is another way to solve collisions. With open addressing, if we want to store an element but there is already an element in that bucket, the element is stored in the next available bucket. This can be done in many different ways, but we will not explain open addressing any further here.

Conclusion
Hash Tables are powerful tools in programming, helping you to manage and access data efficiently.

Whether you use a Hash Set or a Hash Map depends on what you need: just to know if something is there, or to find detailed information about it.
"""
my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10
    
def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)
        
def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contains('Stuart'))

#Python