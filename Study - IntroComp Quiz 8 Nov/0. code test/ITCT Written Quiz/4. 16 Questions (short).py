# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:55:28 2018

@author: Tim
"""

square_list = [i**2 for i in range(101) if i**2%3 == 0]

#1: Recursion
def f(n):
    if n== 0:                   #base case
        return 1
    else:
        return n * f(n-1)       #recursive step

#2: Reverser
def reverser(a_str):
    if len(a_str) == 1:
        return a_str
    else:
        new_str = reverser(a_str[1:]) + a_str[0]
        return new_str

# Note that Recursive functions can be Inefficient


#3: Complete Binary Tree (CBT)
tree = [[[7], 1, [9]], 3, [[8,], 2, [4]]]


#4: Number of Nodes
def numOfNodes(t):
    if len(t) == 1:
        return 1;
    else:
        numLeft = numOfNodes(t[0])
        numRight = numOfNodes(t[2])
        
        return (numLeft + numRight + 1)

#5: Sum of Nodes
def sumOfNodes(t):
    if len(t) == 1:
        return t[0];
    else:
        sumLeft = sumOfNodes(t[0])
        sumRight = sumOfNodes(t[2])
        return (t[1] + sumLeft + sumRight)

#6: Max Node
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

#7: Mirror the Tree
def mirror(t):
    if len(t) == 1:
        return t
    else:
        parent = t[1]
        mirrorLtree = mirror(t[0])
        mirrorRtree = mirror(t[2])
        return [mirrorRtree, parent, mirrorLtree]

#8: Print the Tree
def printTree(t, level):
    if len(t) == 1:
        print(" "*level, end="")
        print (t[0])
    else:
        printTree(t[2], level + 1)
        
        print(" "*level, end="")
        print(t[1])
        
        printTree(t[0], level + 1)


#9: Linear Search
foodList = ['Bakery Cuisine', 'Subway', 'Peach Garden Chinese Restaurant',
            'Mr Bean', 'Pizza Hut', 'The Soup Spoon Union',
            'North Spine Food Court']

for item in foodList:
    if item == 'Pizza Hut':
        print('Pizza Hut in list')
        break

foodList = print ("Index for Pizza Hut : ", foodList.index("Pizza Hut"))

try: foodList = print ("Index for Pizza Hut : ", foodList.index("pizza Hut"))
except: AttributeError



#10: Binary Search
def binarySearch(items, target):
    #start with entire list
    low = 0
    high = len(items) - 1
    
    #Repeatedly subdivide the list until the target is found
    while low <= high:
        mid = (low + high) //2
        #compares middle item with search key
        if items[mid] == target:
            return True
        elif target < items[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


#11: Recursive Binary Search
def binary_search(items, target, low = 0, high = None):
    if high == None:
        high = len(items) - 1
    
    if low > high:
        return False
    
    mid = (low + high)//2
    if target == items[mid]:
        return True
    
    elif target > items[mid]:
        return binary_search(items, target, low = (mid+1), high = high)
    else:
        return binary_search(items, target, low = low, high = (mid - 1))

#test
numbers = range(1,20,1)
search_key = 7

if (binary_search(numbers, search_key)):
    print(search_key, "is in the list")
else:
    print(search_key, "is not in the list.")


#12: Calculate 1 - 2 + 3 - 4 + 5...-10
def addOddsubtractEven(n):
    result = 0
    for i in range (1,n+1):
        if i%2 == 1:
            result = result + i
        else:
            result = result - i
    print(result)
    

#13: The Sorted Function

restaurant_info = [['Kentucky', 15, 6, 'Fried chicken'],
                   ['Macdonald', 12, 5, 'Burger'],
                   ['Subway', 13, 7, 'Sandwiches']]

from operator import itemgetter

sort_info = sorted (restaurant_info, key = itemgetter(1))
#print('sort by distance', sort_info)

#To print all different sort fields

sort_field = ['name', 'distance', 'price', 'food']

for i in range(len(sort_field)):
    sort_info = sorted(restaurant_info, key = itemgetter(i))
#    print('sort by', sort_field[i], sort_info)

'''Sorted: Takes in a list and itemgetter(index). Used to sort columns other than the index'''

#14: Bubblesort
def bubbleSort(alist):
    for passnum in range(len(alist)-1):
#       for i in range(len(alist)-1):    --> After the first pass, the largest Number is already sorted.
        for i in range(len(alist)-passnum-1):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#15: Stop the sort, if everything is already sorted.
def bubbleSortII(alist):
    for passnum in range(len(alist)-1):
        swapped = False
        for i in range(len(alist)-1):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                swapped = True
        if not swapped:             #If nothing changes on a pass, it is sorted
            break;

'''alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)'''


#16: Mergesort:
#1. Break in Halves until left with one element to mergeSort
#2. Append lower number to list. Repeat until only one list remains.
#3. If a list has anything remaining, it must be sorted. Append whole list.
#4. Return a list.

def mergesort(list_of_items):
    list_len = len(list_of_items)
#    print(list_len)
    #base case
    if list_len < 2:
        return list_of_items
    
    #break in halves
    left_list = list_of_items[:list_len//2]
    right_list = list_of_items[list_len//2:]
#    print(right_list)
    #merge sort left and right list recursively
    left_list = mergesort(left_list)
#    print(left_list)
    right_list = mergesort(right_list)
    print(right_list)
    return merge(left_list, right_list)

def merge(left_list, right_list):
    result_list = []
    
    #while left and right list have elements
    while left_list and right_list:
#        print(left_list)
        if left_list[0] < right_list[0]:
            result_list.append(left_list[0])
#            print(left_list)
#            print(result_list)
            left_list.pop(0)
        else:
            result_list.append(right_list[0])
            right_list.pop(0)
    
    #if either list still contains elements, it is already sorted and we can append contents
    if left_list:
        result_list.extend(left_list)
    elif right_list:
        result_list.extend(right_list)

list_test = [21,1,26,45,3,3,4,27,43,34,46,40]

new_list = mergesort(list_test)
print(new_list)
#for item in new_list:
#    print(item, end=', ')



