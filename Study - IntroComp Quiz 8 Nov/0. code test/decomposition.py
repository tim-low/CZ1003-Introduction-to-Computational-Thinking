# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:07:32 2018

@author: Tim
"""

square_list = [i**2 for i in range(101) if i**2%3 == 0]

#Recursion
def f(n):
    if n== 0:                   #base case
        return 1
    else:
        return n * f(n-1)       #recursive step

# Decompose the problem into subproblems
# Call the Function to solve each subproblem
# Compose the final result, and return it


def reverser(a_str):
    if len(a_str) == 1:
        return a_str
    else:
        new_str = reverser(a_str[1:]) + a_str[0]
        return new_str

# Note that Recursive functions can be Inefficient


# Complete Binary Tree (CBT)
tree = [[[7], 1, [9]], 3, [[8,], 2, [4]]]

#Number of Nodes
def numOfNodes(t):
    if len(t) == 1:
        return 1;
    else:
        numLeft = numOfNodes(t[0])
        numRight = numOfNodes(t[2])
        
        return (numLeft + numRight + 1)

#Sum of Nodes
def sumOfNodes(t):
    if len(t) == 1:
        return t[0];
    else:
        sumLeft = sumOfNodes(t[0])
        sumRight = sumOfNodes(t[2])
        return (t[1] + sumLeft + sumRight)

#Max Node
def maxNode(t):
    if len(t) == 1:
        return t[0];
    else:
        leftMax = maxNode(t[0])
        rightMax = maxNode(t[2])
        
        maxValue = t[1]
        if leftMax > maxValue:
            maxValue = leftMax
        if rightMax > maxValue:
            maxValue = rightMax
        return maxValue

def minNode(t):
    if len(t) == 1:
        return t[0];
    else:
        leftMin = minNode(t[0])
        rightMin = minNode(t[2])
        
        minValue = t[1]
        if leftMin < minValue:
            minValue = leftMin
        if rightMin < minValue:
            minValue = rightMin
        return minValue

#Mirror the Tree
def mirror(t):
    if len(t) == 1:
        return t
    else:
        parent = t[1]
        mirrorLtree = mirror(t[0])
        mirrorRtree = mirror(t[2])
        return [mirrorRtree, parent, mirrorLtree]

#Print the Tree
def printTree(t, level):
    if len(t) == 1:
        print(" "*level, end="")
        print (t[0])
    else:
        printTree(t[2], level + 1)
        
        print(" "*level, end="")
        print(t[1])
        
        printTree(t[0], level + 1)
        
