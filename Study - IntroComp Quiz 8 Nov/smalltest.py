# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:17:56 2018

@author: Tim
"""
'''
scores1 = [10,11,15,20,55,76,90,84]
scores2 = [4,9,12,98,35,42,4,5,10]

all_scores = [scores1, scores2]

def scoreCheck(all_scores):
    max_scores = []
    avg_scores = []
    for i in all_scores:
        max_scores.append(max(i))
        avg_scores.append(sum(i)/len(i))
    print ("The highest average score is ", max(avg_scores), \
           " and the highest maximum score is ", max(max_scores))

scoreCheck(all_scores)
'''

#Ex4.3: Use of List Comprehension
'''
def x_square_div_by_3():
    result_list = []
    for i in range(1,100):
        if (i**2)%3 == 0:
            result_list.append(i**2)
    print (result_list)

x_square_div_by_3()
'''

#Ex4.4: Use of Dictionary
def query(database):
    


gradebook = {
        "FS1":{
                "1":45
                "2":75
                "3":75
                "4":75
                }