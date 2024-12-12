"""
Binary Trees
A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, a left child node and a right child node.

This restriction, that a node can have a maximum of two child nodes, gives us many benefits:

Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
Binary Trees can be represented as arrays, making the tree more memory efficient.
Use the animation below to see how a Binary Tree looks, and what words we use to describe it.

Types of Binary Trees
There are different variants, or types, of Binary Trees worth discussing to get a better understanding of how Binary Trees can be structured.

The different kinds of Binary Trees are also worth mentioning now as these words and concepts will be used later in the tutorial.

Below are short explanations of different types of Binary Tree structures, and below the explanations are drawings of these kinds of structures to make it as easy to understand as possible.

A balanced Binary Tree has at most 1 in difference between its left and right subtree heights, for each node in the tree.

A complete Binary Tree has all levels full of nodes, except the last level, which is can also be full, or filled from left to right. The properties of a complete Binary Tree means it is also balanced.

A full Binary Tree is a kind of tree where each node has either 0 or 2 child nodes.

A perfect Binary Tree has all leaf nodes on the same level, which means that all levels are full of nodes, and all internal nodes have two child nodes.The properties of a perfect Binary Tree means it is also full, balanced, and complete.
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def orderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ") # pre-order traversal
    orderTraversal(node.left) 
    print(node.data, end=", ") # in-order traversal
    orderTraversal(node.right)
    print(node.data, end=", ") # post-order traversal

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Traverse
orderTraversal(root)

#Python
