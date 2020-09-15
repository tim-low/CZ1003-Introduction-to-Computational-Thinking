# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 10:14:06 2018

@author: Tim
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 06 00:18:13 2018

@author: Tim
"""

import pygame
import math


def update_UI():  # update ui portion only
    pygame.display.update((1221, 0, 400, 1221))


def display_UI(screen):
    pygame.draw.rect(screen, (255, 255, 255), (1221 + 50, 50, 300, 50))  # draw rectangle
    display_Text(screen, "Search by?", (1221 + 50, 50))


def display_Canteens(screen, canteens):
    for i in range(len(canteens)):
        display_Text(screen, str(i + 1) + "." + canteens[i][0], (1231, 150 + i * 50), 20)


def clear_UI(screen):
    pygame.draw.rect(screen, (200, 200, 200), (1221, 0, 400, 1221))  # draw rectangle


def display_Text(screen, text_string, position_tuple, fontsize=30):
    text_font = pygame.font.Font('Arial.ttf', fontsize)  # initialize new font object named text_font
    text_surface = text_font.render(text_string, False, (0, 0, 0))  # creates new surface with text rendered on it
    screen.blit(text_surface, position_tuple)  # draw text_surface onto screen


def display_map():
    introScreenImage = pygame.image.load("NtuMap.png")  # image size is(1221,862)
    screen = pygame.display.set_mode((1221 + 400, 862))
    pygame.display.set_caption("NTU_F&B")  # sets window caption to NTU_F&B
    screen.fill((200, 200, 200))

    screen.blit(introScreenImage, (0, 0))  # draw introScreenImage onto screen

    pygame.display.flip()  # Update the full display Surface to the screen
    return screen


# def get_user_location():  #Get user location either though console input or mouse click
#   pass

def distance_a_b(location_of_a, location_of_b):  # The function calculate the distance between two points.
    return math.sqrt((location_of_b[0] - location_of_a[0]) ** 2 + (location_of_b[1] - location_of_a[1]) ** 2)


def sort_distance(user_location, canteens_list,
                  fontsize=15):  # Display the sorted distances from user’s current location to each canteen in ascending order.
    for passnum in range(len(canteens_list) - 1):
        swapped = False
        for i in range(len(canteens_list) - 1 - passnum):
            if distance_a_b(user_location, canteens_list[i][1]) > distance_a_b(user_location, canteens_list[i + 1][1]):
                temp = canteens_list[i]
                canteens_list[i] = canteens_list[i + 1]
                canteens_list[i + 1] = temp
                swapped = True
        # print("pass", passnum + 1, ":", canteens_list)
        if not swapped:
            break
    for i in range(len(canteens_list)):  # add distance into the description of each location
        description_str = "Distance:" + str(int(float(distance_a_b(user_location, canteens_list[i][1])) * 10)) + "m ," + \
                          canteens_list[i][0]  # dist * 10 1 pixel = 10m
        display_Text(screen, str(i + 1) + "." + description_str, (1231, 150 + i * 50), fontsize)


def search_by_food(foodname, foodlist_canteens,
                   canteens):  # Search all canteens and display the canteens with wanted food
    yPosition = 0
    for i in range(len(foodlist_canteens)):  # Traverse all the canteens
        for j in range(len(foodlist_canteens[i])):
            if (foodlist_canteens[i][j] == foodname):  # you found it
                display_Text(screen, str(i + 1) + "." + canteens[i][0], (1231, 150 + yPosition * 50), 20)
                yPosition += 1
                break


def sort_by_rank(ranklist_canteens):  # sort the canteens by rank and return the sorted list
    for passnum in range(len(canteens_list) - 1):
        swapped = False
        for i in range(len(canteens_list) - 1 - passnum):
            if canteens_list[i][3] > canteens_list[i + 1][3]:
                temp = canteens_list[i]
                canteens_list[i] = canteens_list[i + 1]
                canteens_list[i + 1] = temp
                swapped = True
        # print("pass", passnum + 1, ":", canteens_list)
        if not swapped:
            break


def Search_by_price(price, foodlist_canteens):  # Search all canteens to return the food within the searched range
    pass


def displayPriceInstr(screen):  # Ask user for budget
    pygame.draw.rect(screen, (255, 255, 255), (1250, 150, 355, 50))
    display_Text(screen, "Choose your budget below", (1250, 150))
    pygame.draw.rect(screen, (255, 255, 255), (1285, 225, 40, 40))
    display_Text(screen, "$3", (1290, 230), fontsize=26)
    pygame.draw.rect(screen, (255, 255, 255), (1385, 225, 40, 40))
    display_Text(screen, "$4", (1390, 230), fontsize=26)
    pygame.draw.rect(screen, (255, 255, 255), (1485, 225, 40, 40))
    display_Text(screen, "$5", (1490, 230), fontsize=26)
    pygame.draw.rect(screen, (255, 255, 255), (1345, 285, 40, 40))
    display_Text(screen, "$6", (1350, 290), fontsize=26)
    pygame.draw.rect(screen, (255, 255, 255), (1445, 285, 40, 40))
    display_Text(screen, "$7", (1450, 290), fontsize=26)


def Mousecoordinate():  # To return coordinate of a mouseclick
    return pygame.mouse.get_pos()


def Update_information():  # Optional: allow use to update information of each canteen
    pass


def transport(user_location,
              dest_location):  # Optional: allow use to get transport information from current location to the destination
    pass


# initialise variables
keep_looping = True
stateCriteria_int = -1  # 0 if program is asking for the user location , 1 if price is clicked, 2 if rank is clicked , 3 if food is clicked , -1 if program is asking for criteria selection ,-2 if program is doing nothing
criteria_string = ["Distance", "Price", "Rank", "Food"]
criteriaHeader_string = ["click user location", "Sorted by Price", "Sorted by Rank", "Sorted by Food"]
user_location = [0, 0]
canteens_list = [["Food Court 1 , Daily: 7am to 9pm", (687, 630), 6.1, 1],
                 # canteens_list = [description of location , (x,y) coordinates of location , price , rank : 1 is the best  ]
                 ["Food Court 2 , Daily: 7am to 9pm", (755, 514), 4.7, 2],
                 ["Food Court 9 , Daily: 7am to 9pm", (976, 294), 5.6, 3],
                 ["Food Court 11 , Daily: 7am to 9pm", (1168, 212), 4.2, 6],
                 ["Food Court 13 , Daily: 7am to 9pm", (690, 90), 4, 5],
                 ["Food Court 14 , Daily: 7am to 9pm", (823, 101), 3, 4]]  # , 13 , 14 , 2 ,1 ,9 ,11

foodlist_canteens = [["Chinese", "Western", "Japanese", "Korean", "Indian", "Malay"],  # Canteen 1
                     ["Chinese", "Western", "Japanese", "Korean", "Indian", "Malay"],
                     ["Japanese", "Korean", "Indian", "Malay"],
                     ["Chinese", "Western", "Japanese", "Korean", "Indian", "Malay"],
                     ["Chinese", "Western", "Indian", "Malay"],
                     ["Chinese", "Western", "Japanese", "Korean", "Indian"]
                     ]
button_width = 150
button_height = 50
button_pos = [(1271, 150), (1271, 210), (1271, 270), (1271, 330), (1271, 390), (1271, 450)]
# main program
pygame.init()
screen = display_map()
display_UI(screen)
# sort_distance((0,0),canteens_list)
while keep_looping:
    mouse = Mousecoordinate()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_looping = False

        if stateCriteria_int == 3:  # if food is clicked
            for food in range(len(foodlist_canteens[0])):
                if button_pos[food][0] + button_width > mouse[0] > button_pos[food][0] and button_pos[food][
                    1] + button_height > mouse[1] > button_pos[food][1]:
                    pygame.draw.rect(screen, (225, 225, 225), (
                    button_pos[food][0], button_pos[food][1], button_width, button_height))  # draw rectangle
                    # hoverFlag = food
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        # check if user left clicked
                        print("Clicked")
                        stateCriteria_int = 4 + food
                        clear_UI(screen)
                        display_UI(screen)
                        print(food)
                        break

                else:
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (button_pos[food][0], button_pos[food][1], button_width, button_height))

                display_Text(screen, "-" + foodlist_canteens[0][food], (button_pos[food][0], button_pos[food][1]))

            """if event.type == pygame.MOUSEBUTTONUP and hoverFlag > -1 and event.button ==1:

                # check if user left clicked
                print("Clicked")
                stateCriteria_int = 4 + hoverFlag"""

        if stateCriteria_int == 4:
            search_by_food("Chinese", foodlist_canteens, canteens_list)

        if stateCriteria_int == 5:
            search_by_food("Western", foodlist_canteens, canteens_list)

        if stateCriteria_int == 6:
            search_by_food("Japanese", foodlist_canteens, canteens_list)

        if stateCriteria_int == 7:
            search_by_food("Korean", foodlist_canteens, canteens_list)
        if stateCriteria_int == 8:
            search_by_food("Indian", foodlist_canteens, canteens_list)
        if stateCriteria_int == 9:
            search_by_food("Malay", foodlist_canteens, canteens_list)
        # stateCriteria_int = -2
        # display_Canteens(screen , canteens_list)

        if stateCriteria_int == -1:  # true if user is choosing criteria
            for criterion in range(len(criteria_string)):
                if button_pos[criterion][0] + button_width > mouse[0] > button_pos[criterion][0] and \
                        button_pos[criterion][1] + button_height > mouse[1] > button_pos[criterion][
                    1]:  # BUTTON if mouse is hovering over a button
                    pygame.draw.rect(screen, (225, 225, 225), (
                    button_pos[criterion][0], button_pos[criterion][1], button_width, button_height))  # draw rectangle
                    display_Text(screen, "-" + criteria_string[criterion],
                                 (button_pos[criterion][0], button_pos[criterion][1]))

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check if user left clicked
                        stateCriteria_int = criterion
                        choosing_CriteriaState = False

                        clear_UI(screen)
                        pygame.draw.rect(screen, (255, 255, 255), (1221 + 50, 50, 300, 50))
                        display_Text(screen, criteriaHeader_string[criterion], (1221 + 50, 50))

                        break
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (
                    button_pos[criterion][0], button_pos[criterion][1], button_width, button_height))  # draw rectangle
                    display_Text(screen, "-" + criteria_string[criterion],
                                 (button_pos[criterion][0], button_pos[criterion][1]))
        else:

            if 1221 + 30 > mouse[0] > 1221 and 0 + 30 > mouse[1] > 0:
                pygame.draw.rect(screen, (225, 225, 225), (1221, 0, 30, 30))  # draw rectangle
                display_Text(screen, "X", (1221 + 5, 0))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check if user left clicked
                    stateCriteria_int = -1
                    clear_UI(screen)
                    display_UI(screen)
            else:
                pygame.draw.rect(screen, (255, 255, 255), (1221, 0, 30, 30))  # draw rectangle
                display_Text(screen, "X", (1221 + 5, 0))

        if stateCriteria_int == 0:  # true if program is asking for the user location

            if 1221 > mouse[0] > 0 and 862 > mouse[1] > 0:  # MAP if mouse is hovering over the map
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # check if user left clicked
                    user_location = [mouse[0], mouse[1]]
                    location_GetState = False
                    print("userlocation saved")
                    # compare distance of different locations and display the nearest to furthest
                    sort_distance(user_location, canteens_list)
                    stateCriteria_int = -2  # program not doing anything but wait for the user to go back to selection state

        if stateCriteria_int == 1:  # if price is clicked
            displayPriceInstr(screen)
            update_UI()

            price_list = []  # contains all the prices of the canteens
            for canteen in canteens_list:
                price_list.append(canteen[2])

            foundlist = []  # to store canteens that fit the budget criteria

            listforprices = [[1285, 1285 + 40, 225, 225 + 40, "$3", (1290, 230), 3],
                             [1385, 1385 + 40, 225, 225 + 40, "$4", (1390, 230), 4],
                             [1485, 1485 + 40, 225, 225 + 40, "$5", (1490, 230), 5],
                             [1345, 1345 + 40, 285, 285 + 40, "$6", (1350, 290), 6],
                             [1445, 1445 + 40, 285, 285 + 40, "$7", (1450, 290), 7]]

            for number in range(3, 8):
                listtocheck = listforprices[number - 3]  # choose sublist in listforprices
                if listtocheck[0] < mouse[0] < listtocheck[1] and listtocheck[2] < mouse[1] < listtocheck[3]:
                    pygame.draw.rect(screen, (225, 225, 225), (listtocheck[0], listtocheck[2], 40, 40))
                    display_Text(screen, listtocheck[4], listtocheck[5], fontsize=26)
                    pricetocheck = listtocheck[6]

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # user clicks their budget
                        for price in price_list:
                            if pricetocheck >= price:
                                for canteen in canteens_list:
                                    if price == canteen[2]:
                                        foundlist.append(canteen[0])
                                        for foundcanteen in range(len(foundlist)):
                                            displaylist = str(foundlist[foundcanteen])
                                            display_Text(screen, str(foundcanteen + 1) + "." + displaylist,
                                                         (1250, 400 + foundcanteen * 50),
                                                         fontsize=20)  # display canteens with prices within the budget chosen

        if stateCriteria_int == 2:  # if rank is clicked

            sort_by_rank(canteens_list)
            display_Canteens(screen, canteens_list)

        update_UI()

# End

pygame.quit()