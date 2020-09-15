# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:04:25 2018

@author: Tim
"""
#PasswordChecker
'''

'''

#Highest Average and Maximum
scores1 = [10,11,15,20,55,76,90,84]
scores2 = [4,9,12,98,35,42,4,5,10]

all_scores = [scores1, scores2]

def scoreCheck(all_scores):
    max_scores = []
    avg_scores
    for i in all_scores:
        max_scores.append(max(i))
    print (maxscores)


def inputRecord():
    
def query():
    
def listGrades():
    
def maxGrade():
    
    
#Show Options
#no input
#no output
def showMsg():
    print("Welcome to the grading system! Please enter your option:")
    print("1: input record")
    print("2: query a student")
    print("3: list grades in a group")
    print("4: get max in a group")
    print("5: list all group names")
    print("6: exit")

#Available Options
def gradeSystem():
    INPUT = 1
    QUERY = 2
    LIST = 3
    MAX = 4
    LISTALLGROUPS = 5
    EXIT = 6
    
    option = INPUT
    
    while option != EXIT:
        showMsg()
        option = int(input("option: "))
        
        if option == INPUT:
            groupName = input("Please input the group name: ")
            sID = int(input("Please input the student id: "))
            score = int(input("Please input the score: "))
            
            inputRecord(grades, groupName, sID, score)
        
        elif option == QUERY:
            groupName = input("Please input the group name: ")
            sID = int(input("Please input the student id"))
            
            score = scoresInGroup = query(grades, groupName, sID)
            
            print("The student's scores: ", score)
            
        elif option == LIST:
            groupName = input("Please input the group name: ")
            
            scoresInGroup = listGrades(grades, groupName)
            
            print("The scores in ", groupName, ":", end = "")
            print(scoresInGroup)
            
        elif option == MAX:
            groupName = input("Please input the group name: ")
            highestScore = maxGrade(grades, groupName)
            
            print("The highest scores in ", groupName, ":", highestScore)

gradebook = 
gradesystem()