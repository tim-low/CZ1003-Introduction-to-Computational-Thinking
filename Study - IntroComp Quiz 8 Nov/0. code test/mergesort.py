# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Calculate 1 - 2 + 3 - 4 + 5...-10
def addOddsubtractEven(n):
    result = 0
    for i in range (1,n+1):
        if i%2 == 1:
            result = result + i
        else:
            result = result - i
    print(result)
    

# The Sorted Function

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

#Bubblesort
def bubbleSort(alist):
    for passnum in range(len(alist)-1):
#       for i in range(len(alist)-1):    --> After the first pass, the largest Number is already sorted.
        for i in range(len(alist)-passnum-1):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

#Stop the sort, if everything is already sorted.
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


#Mergesort:
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
