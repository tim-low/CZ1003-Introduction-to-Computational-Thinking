# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:55:28 2018

@author: Tim
"""
#0: Print all x**2 for 1-100 if x**2 is divisible by 3




#1: Recursion: Get nth Fibonacci Number



#2: Reverser: take a string and reverse it



#3: Complete Binary Tree (CBT): Represent a Binary Tree



#4: Number of Nodes: Takes a Tree and returns the number of nodes




#5: Sum of Nodes: Takes a Tree and returns the sum of nodes




#6: Max/Min Node: Takes a Tree and returns the Max/Min node of the tree



#7: Mirror the Tree



#8: Print the Tree: Takes a Tree and a level(how far right)



#9: Linear Search: Print: If Pizza Hut in list, what Index it is. Have Exception if not in list.



#10: Binary Search: Take list, target, and return True or False




#11: Recursive Binary Search: Take list, target, and return True or False



#test
numbers = range(1,20,1)
search_key = 7

if (binary_search(numbers, search_key)):
    print(search_key, "is in the list")
else:
    print(search_key, "is not in the list.")


#12: Calculate 1 - 2 + 3 - 4 + 5...-10
def addOddsubtractEven(n):
    
    

#13: The Sorted Function

restaurant_info = [['Kentucky', 15, 6, 'Fried chicken'],
                   ['Macdonald', 12, 5, 'Burger'],
                   ['Subway', 13, 7, 'Sandwiches']]


#15: BubbleSort

'''alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)'''


#16: Mergesort:
#1. Break in Halves until left with one element to mergeSort
#2. Append lower number to list. Repeat until only one list remains.
#3. If a list has anything remaining, it must be sorted. Append whole list.
#4. Return a list.


list_test = [21,1,26,45,3,3,4,27,43,34,46,40]


new_list = mergesort(list_test)
print(new_list)




