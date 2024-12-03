"""
Queues
A queue is a data structure that can hold many elements.

Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket. This way of organizing elements is called FIFO: First In First Out.

Basic operations we can do on a queue are:

Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.
Experiment with these basic operations in the queue animation above.

Queues can be implemented by using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing for e-tickets, or to create algorithms for breadth-first search in graphs.

Queues are often mentioned together with Stacks, which is a similar data structure described on the previous page.
"""
queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Dequeue
element = queue.pop(0)
print("Dequeue: ", element)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))

"""
But to explicitly create a data structure for queues, with basic operations, we should create a queue class instead. 
This way of creating queues in Python is also more similar to how queues can be created in other programming languages 
like C and Java.
"""

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", myQueue.queue)

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())

"""
Queue Implementation using Linked Lists
Reasons for using linked lists to implement queues:

Dynamic size: The queue can grow and shrink dynamically, unlike with arrays.
No shifting: The front element of the queue can be removed (enqueue) without having to shift other elements in the memory.
Reasons for not using linked lists to implement queues:

Extra memory: Each queue element must contain the address to the next element (the next linked list node).
Readability: The code might be harder to read and write for some because it is longer and more complex.
This is how a queue can be implemented using a linked list.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())