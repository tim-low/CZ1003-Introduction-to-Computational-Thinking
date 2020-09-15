# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 07:23:16 2018

@author: Tim
"""
import pygame
import math

TheSoupUnion_Price = [6.5, 18.8]
FoodCourt1_Price = [3, 10]
FoodCourt2_Price = [4, 10]
FoodCourt9_Price = [3, 10]
FoodCourt11_Price = [3, 10]
FoodCourt13_Price = [4, 10]
FoodCourt14_Price = [3, 10]
FoodCourt16_Price = [4, 10]
AnandaKitchen_Price = [6, 12]
FoodgleFoodCourt_Price = [3, 11]
NorthHillFoodCourt_Price = [3, 10]
PioneerFoodCourt_Price = [4, 10]
QuadCafe_Price = [4, 10]
NorthSpineFoodCourt_Price = [4, 10]
PeachGardenChineseRestaurant_Price = [20, 100]
PEN_N_INC_Price = [12, 30]
Koufu_theSouthSpine_Price = [3, 10]
TheSandwichGuys_Price = [5, 10]
TheHouseSteamBoatRestaurant_Price = [15, 20]
Subway_Price = [4, 10]
StarbucksCoffee_Price = [6, 10]
PizzaHutExpress_Price = [4, 10]
PaiksBibim_Price = [6, 12]
MrBean_Price = [2, 6]
McDonalds_Price = [5, 10]
LongJohnSilvers_Price = [5, 10]
KFC_Price = [6, 10]
GrandeCibo_Price = [6, 12]
EachACup_Price = [3, 6]
BakeryCuisine_Price = [2, 5]


#food
FoodCourt1_Food = ['Chicken rice', 'Mixed vegetable rice', 'Western food']
FoodCourt2_Food = ['Chicken rice', 'Korean food', 'Japanese food', 'Banmian', 'Mixed vegetable rice']
FoodCourt9_Food = ['Fried rice', 'Hor fun', 'Noodles', 'Chinese food']
TheSoupUnion_Food = ['Soup']
FoodCourt11_Food = ['Indian cuisine', 'Korean food', 'Fried rice']
FoodCourt13_Food = ['Mixed vegetable rice', 'Korean food', 'Fried rice']
FoodCourt14_Food = ['Malay cuisine', 'Banmian', 'Noodle', 'Fish soup', 'Mixed vegetable rice']
FoodCourt16_Food = ['Indian cuisine', 'Vegetarian food', 'Mixed vegetable rice', 'Carrot cake', 'Japanese food']
AnandaKitchen_Food = ['Indian cuisine']
FoodgleFoodCourt_Food = ['Chicken rice','Malay cuisine']
NorthHillFoodCourt_Food = ['Mixed vegetable rice', 'Noodle', 'Malay cuisine', 'Chicken rice', 'Yong tau foo', 'Indian cuisine', 'Carrot cake']
PioneerFoodCourt_Food = ['Mixed vegetable rice', 'Vegetarian']
QuadCafe_Food = ['Mixed vegetable rice', 'Chinese food', 'Korean food', 'Noodle', 'Mini wok']
NorthSpineFoodCourt_Food = ['Mixed vegetable rice', 'Malay cuisine', 'Chicken rice', 'Duck rice', 'Ban mian', 'Vegetarian', 'International food', 'Mala hot pot', 'Mini wok', 'Yong tau foo']
PeachGardenChineseRestaurant_Food = ['Chinese cuisine']
PEN_N_INC_Food = ['Western food','Pasta','Dessert','Burger']
Koufu_theSouthSpine_Food = ['Mixed vegetable rice', 'Noodles', 'Vegetarian food', 'Chicken rice', 'Malay cuisine', 'Ban mian']
TheSandwichGuys_Food = ['Sandwich']
TheHouseSteamBoatRestaurant_Food = ['Steam boat', 'Soup']
Subway_Food = ['Sandwich']
StarbucksCoffee_Food = ['Coffee', 'Pastries']
PizzaHutExpress_Food = ['Pizza']
PaiksBibim_Food = ['Korean food', 'Rice']
MrBean_Food = ['Soya milk', 'Soy pancakes', 'Soy ice cream']
McDonalds_Food = ['Burger', 'French fries']
LongJohnSilvers_Food = ['Fried fish']
KFC_Food = ['Fried chicken']
GrandeCibo_Food = ['Pizza','Pasta']
EachACup_Food = ['Bubble Tea']
BakeryCuisine_Food = ['Bread', 'Pastries']

#Area
TheSoupUnion_Area = [(323, 239)]
FoodCourt1_Area = [(487, 432), (497, 436), (492, 443), (482, 452), (476, 449), (483, 438)]
FoodCourt2_Area = [(529, 351), (537, 357), (543, 364), (536, 373), (529, 364), (521, 355)]
FoodCourt9_Area = [(659, 227), (673, 230), (682, 227), (681, 216), (669, 215)]
FoodCourt11_Area = [(801, 165), (800, 173), (791, 181), (777, 179), (776, 166)]
FoodCourt13_Area = [(493, 88), (500, 97), (493, 103), (483, 97)]
FoodCourt14_Area = [(576, 108), (565, 106), (565, 93), (577, 91), (592, 98), (588, 110)]
FoodCourt16_Area = [(436, 141), (449, 139), (449, 152), (437, 152)]
AnandaKitchen_Area = [(799, 228)]
FoodgleFoodCourt_Area = [(741, 119)]
NorthHillFoodCourt_Area = [(838,260)]
PioneerFoodCourt_Area = [(561,553)]
QuadCafe_Area = [(199, 280)]
NorthSpineFoodCourt_Area = [(281, 226)]
PeachGardenChineseRestaurant_Area = [(298, 205)]
PEN_N_INC_Area = [(302, 211)]
Koufu_theSouthSpine_Area = [(235, 453), (221, 459), (207, 455)]
TheSandwichGuys_Area = [(319, 242)]
TheHouseSteamBoatRestaurant_Area = [(320, 240)]
Subway_Area = [(293, 227)]
StarbucksCoffee_Area = [(288, 221)]
PizzaHutExpress_Area = [(302, 210)]
PaiksBibim_Area = [(320, 240)]
MrBean_Area = [(315, 235)]
McDonalds_Area = [(301, 228)]
LongJohnSilvers_Area = [(290, 215)]
KFC_Area = [(296, 223)]
GrandeCibo_Area = [(315, 249)]
EachACup_Area = [(316, 240)]
BakeryCuisine_Area = [(318, 246)]


#Time
# place_Time=[[open],[close]]

TheSoupUnion_Time = [11, 21]
FoodCourt1_Time =[7,21]
FoodCourt2_Time = [7, 21]
FoodCourt9_Time = [7, 21]
FoodCourt11_Time = [7, 21]
FoodCourt11_Time = [7, 21]
FoodCourt13_Time = [7, 21]
FoodCourt14_Time = [7, 21]
FoodCourt16_Time = [7, 21]
AnandaKitchen_Time = [12, 22]
FoodgleFoodCourt_Time = [7, 21]
NorthHillFoodCourt_Time = [7, 21]
PioneerFoodCourt_Time = [7, 21]
QuadCafe_Time = [7, 21]
NorthSpineFoodCourt_Time = [7, 21]
PeachGardenChineseRestaurant_Time = [11, 22]
PEN_N_INC_Time = [11, 23]
Koufu_theSouthSpine_Time = [7, 21]
TheSandwichGuys_Time = [10, 20]
TheHouseSteamBoatRestaurant_Time = [9, 21]
Subway_Time = [8, 21]
StarbucksCoffee_Time = [7, 10]
PizzaHutExpress_Time = [11, 20]
PaiksBibim_Time = [10, 21]
MrBean_Time = [7, 20]
McDonalds_Time = [7, 24]
LongJohnSilvers_Time = [7, 22]
KFC_Time = [7, 22]
GrandeCibo_Time = [11, 20]
EachACup_Time = [9, 21]
BakeryCuisine_Time = [7, 21]




#Standard = {'Price Range':,
#            'Coordinates':,
#            'Food':,
#            }
TheSoupUnion = {'Price Range':TheSoupUnion_Price,
                'Coordinates':TheSoupUnion_Area,
                'Food':TheSoupUnion_Food,
                'Operating Hours': TheSoupUnion_Time,
                'Votes': 30
                }

FoodCourt1 = {'Price Range':FoodCourt1_Price,
              'Coordinates':FoodCourt1_Area,
              'Food':FoodCourt1_Food,
              'Operating Hours':FoodCourt1_Time,
              'Votes': 29
              }

FoodCourt2 = {'Price Range':FoodCourt2_Price,
              'Coordinates':FoodCourt2_Area,
              'Food':FoodCourt2_Food,
              'Operating Hours':FoodCourt2_Time,
              'Votes': 28
                }

FoodCourt9 = {'Price Range':FoodCourt9_Price,
              'Coordinates':FoodCourt9_Area,
              'Food':FoodCourt9_Food,
              'Operating Hours':FoodCourt9_Time,
              'Votes': 27
              }

FoodCourt11 = {'Price Range':FoodCourt11_Price,
               'Coordinates':FoodCourt11_Area,
               'Food':FoodCourt11_Food,
               'Operating Hours':FoodCourt11_Time,
               'Votes': 26
               }

FoodCourt13 = {'Price Range':FoodCourt13_Price,
               'Coordinates':FoodCourt13_Area,
               'Food':FoodCourt13_Food,
               'Operating Hours':FoodCourt13_Time,
               'Votes': 25
               }

FoodCourt14 = {'Price Range':FoodCourt14_Price, 
               'Coordinates':FoodCourt14_Area,
               'Food':FoodCourt14_Food,
               'Operating Hours':FoodCourt14_Time,
               'Votes': 24
               }

FoodCourt16 = {'Price Range':FoodCourt16_Price,
               'Coordinates':FoodCourt16_Area,
               'Food':FoodCourt16_Food,
               'Operating Hours':FoodCourt16_Time,
               'Votes': 23
               }

AnandaKitchen = {'Price Range':AnandaKitchen_Price,
                 'Coordinates':AnandaKitchen_Area,
                 'Food':AnandaKitchen_Food,
                 'Operating Hours':AnandaKitchen_Time,
                 'Votes': 22
                 }

FoodgleFoodCourt = {'Price Range':FoodgleFoodCourt_Price,
                    'Coordinates':FoodgleFoodCourt_Area,
                    'Food':FoodgleFoodCourt_Food,
                    'Operating Hours':FoodgleFoodCourt_Time,
                    'Votes': 21
                    }

NorthHillFoodCourt  = {'Price Range':NorthHillFoodCourt_Price,
                       'Coordinates':NorthHillFoodCourt_Area,
                       'Food':NorthHillFoodCourt_Food,
                       'Operating Hours':NorthHillFoodCourt_Time,
                       'Votes': 20
                       }

PioneerFoodCourt = {'Price Range':PioneerFoodCourt_Price,
                    'Coordinates':PioneerFoodCourt_Area,
                    'Food':PioneerFoodCourt_Food,
                    'Operating Hours':PioneerFoodCourt_Time,
                    'Votes': 19
                    }

QuadCafe = {'Price Range':QuadCafe_Price,
            'Coordinates':QuadCafe_Area,
            'Food':QuadCafe_Food,
            'Operating Hours':QuadCafe_Time,
            'Votes': 18
            }

NorthSpineFoodCourt = {'Price Range':NorthSpineFoodCourt_Price,
                       'Coordinates':NorthSpineFoodCourt_Area,
                       'Food':NorthSpineFoodCourt_Food,
                       'Operating Hours':NorthSpineFoodCourt_Time,
                       'Votes': 17
                       }

PeachGardenChineseRestaurant = {'Price Range':PeachGardenChineseRestaurant_Price,
                                'Coordinates':PeachGardenChineseRestaurant_Area,
                                'Food':PeachGardenChineseRestaurant_Food,
                                'Operating Hours':PeachGardenChineseRestaurant_Time,
                                'Votes': 16
                                }

PEN_N_INC = {'Price Range':PEN_N_INC_Price,
           'Coordinates':PEN_N_INC_Area,
           'Food':PEN_N_INC_Food,
           'Operating Hours':PEN_N_INC_Time,
           'Votes': 15
           }

Koufu_theSouthSpine = {'Price Range': Koufu_theSouthSpine_Price,
                       'Coordinates': Koufu_theSouthSpine_Area,
                       'Food': Koufu_theSouthSpine_Food,
                       'Operating Hours': Koufu_theSouthSpine_Time,
                       'Votes': 14
                       }

TheSandwichGuys = {'Price Range': TheSandwichGuys_Price,
                   'Coordinates': TheSandwichGuys_Area,
                   'Food': TheSandwichGuys_Food,
                   'Operating Hours':TheSandwichGuys_Time,
                   'Votes': 13
                   }

TheHouseSteamBoatRestaurant = {'Price Range': TheHouseSteamBoatRestaurant_Price,
                               'Coordinates': TheHouseSteamBoatRestaurant_Area,
                               'Food': TheHouseSteamBoatRestaurant_Food,
                               'Operating Hours': TheHouseSteamBoatRestaurant_Time,
                               'Votes': 12
                               }

Subway = {'Price Range': Subway_Price,
          'Coordinates': Subway_Area,
          'Food': Subway_Food,
          'Operating Hours': Subway_Time,
          'Votes': 11
          }

StarbucksCoffee = {'Price Range': StarbucksCoffee_Price,
                   'Coordinates': StarbucksCoffee_Area,
                   'Food': StarbucksCoffee_Food,
                   'Operating Hours': StarbucksCoffee_Time,
                   'Votes': 10
                   }

PizzaHutExpress = {'Price Range': PizzaHutExpress_Price,
                   'Coordinates': PizzaHutExpress_Area,
                   'Food': PizzaHutExpress_Food,
                   'Operating Hours': PizzaHutExpress_Time,
                   'Votes': 9
                   }

PaiksBibim = {'Price Range': PaiksBibim_Price,
              'Coordinates': PaiksBibim_Area,
              'Food': PaiksBibim_Food,
              'Operating Hours': PaiksBibim_Time,
              'Votes': 8
              }

MrBean = {'Price Range': MrBean_Price,
          'Coordinates': MrBean_Area,
          'Food': MrBean_Food,
          'Operating Hours': MrBean_Time,
          'Votes': 7
          }

McDonalds = {'Price Range': McDonalds_Price,
             'Coordinates': McDonalds_Area,
             'Food': McDonalds_Food,
             'Operating Hours': McDonalds_Time,
             'Votes': 6
             }

LongJohnSilvers = {'Price Range': LongJohnSilvers_Price,
                   'Coordinates': LongJohnSilvers_Area,
                   'Food': LongJohnSilvers_Food,
                   'Operating Hours': LongJohnSilvers_Time,
                   'Votes': 5
                   }

KFC = {'Price Range': KFC_Price,
       'Coordinates': KFC_Area,
       'Food': KFC_Food,
       'Operating Hours': KFC_Time,
       'Votes': 4
       }

GrandeCibo = {'Price Range': GrandeCibo_Price,
              'Coordinates': GrandeCibo_Area,
              'Food': GrandeCibo_Food,
              'Operating Hours': GrandeCibo_Time,
              'Votes': 3
              }

EachACup = {'Price Range': EachACup_Price,
            'Coordinates': EachACup_Area,
            'Food': EachACup_Food,
            'Operating Hours': EachACup_Time,
            'Votes': 2
            }

BakeryCuisine = {'Price Range': BakeryCuisine_Price,
                 'Coordinates': BakeryCuisine_Area,
                 'Food': BakeryCuisine_Food,
                 'Operating Hours': BakeryCuisine_Time,
                 'Votes': 1
                 }


#Overall:
NTU_Food = {'TheSoupUnion':TheSoupUnion,
            'FoodCourt1':FoodCourt1,
            'FoodCourt2':FoodCourt2,
            'FoodCourt9':FoodCourt9,
            'FoodCourt11':FoodCourt11,
            'FoodCourt13':FoodCourt13, 
            'FoodCourt14':FoodCourt14, 
            'FoodCourt16':FoodCourt16, 
            'AnandaKitchen':AnandaKitchen, 
            'FoodgleFoodCourt':FoodgleFoodCourt, 
            'NorthHillFoodCourt':NorthHillFoodCourt, 
            'PioneerFoodCourt':PioneerFoodCourt, 
            'QuadCafe':QuadCafe, 
            'NorthSpineFoodCourt':NorthSpineFoodCourt, 
            'PeachGardenChineseRestaurant':PeachGardenChineseRestaurant, 
            'PEN&INC':PEN_N_INC,
            'Koufu@theSouthSpine':Koufu_theSouthSpine, 
            'TheSandwichGuys':TheSandwichGuys, 
            'TheHouseSteamBoatRestaurant':TheHouseSteamBoatRestaurant,
            'Subway':Subway,
            'StarbucksCoffee':StarbucksCoffee,
            'PizzaHutExpress':PizzaHutExpress,
            'PaiksBibim':PaiksBibim,
            'MrBean':MrBean,
            'McDonalds':McDonalds,
            'LongJohnSilvers':LongJohnSilvers,
            'KFC':KFC,
            'GrandeCibo':GrandeCibo,
            'EachACup':EachACup,
            'BakeryCuisine':BakeryCuisine
            }

rank = {1: ['TheSoupUnion', TheSoupUnion],
        2: ['FoodCourt1', FoodCourt1],
        3: ['FoodCourt2', FoodCourt2],
        4: ['FoodCourt9', FoodCourt9],
        5: ['FoodCourt11', FoodCourt11],
        6: ['FoodCourt13', FoodCourt13],
        7: ['FoodCourt14', FoodCourt14],
        8: ['FoodCourt16', FoodCourt16],
        9: ['AnandaKitchen', AnandaKitchen],
        10: ['FoodgleFoodCourt', FoodgleFoodCourt],
        11: ['NorthHillFoodCourt', NorthHillFoodCourt],
        12: ['PioneerFoodCourt', PioneerFoodCourt],
        13: ['QuadCafe', QuadCafe],
        14: ['NorthSpineFoodCourt', NorthSpineFoodCourt],
        15: ['PeachGardenChineseRestaurant', PeachGardenChineseRestaurant],
        16: ['PEN_N_INC', PEN_N_INC],
        17: ['Koufu_theSouthSpine', Koufu_theSouthSpine],
        18: ['TheSandwichGuys', TheSandwichGuys],
        19: ['TheHouseSteamBoatRestaurant', TheHouseSteamBoatRestaurant],
        20: ['Subway', Subway],
        21: ['StarbucksCoffee', StarbucksCoffee],
        22: ['PizzaHutExpress', PizzaHutExpress],
        23: ['PaiksBibim', PaiksBibim],
        24: ['MrBean', MrBean],
        25: ['McDonalds', McDonalds],
        26: ['LongJohnSilvers', LongJohnSilvers],
        27: ['KFC', KFC],
        28: ['GrandeCibo', GrandeCibo],
        29: ['EachACup', EachACup],
        30: ['BakeryCuisine', BakeryCuisine]
        }
  
list_of_food = ['Chicken rice', 'Mixed vegetable rice', 'Western food','Korean food', 'Japanese food', 'Banmian', 'Mixed vegetable rice',
                'Fried rice', 'Hor fun', 'Noodles', 'Chinese food', 'Soup', 'Indian cuisine', 'Malay cuisine', 'Banmian', 'Noodle',
                'Fish soup', 'Vegetarian food', 'Mixed vegetable rice', 'Carrot cake', 'Yong tau foo', 'Vegetarian', 'Mini wok', 'Duck rice',
                'International food', 'Mala hot pot', 'Chinese cuisine', 'Pasta','Dessert','Burger', 'Ban mian', 'Sandwich', 'Steam boat',
                'Coffee', 'Pastries','Pizza', 'Rice', 'Soya milk', 'Soy pancakes', 'Soy ice cream', 'Burger', 'French fries', 'Fried fish',
                'Fried chicken', 'Bubble Tea', 'Bread', 'Pastries']

#Notes:
#Functions 2-7 are complete.
#Functions 3-6 take in the required inputs, and return a list.

#I have added one parameter to Steffi's restaurant stats: "Votes". This is used to calculate Rank.
#There is no current way to change 'Votes'. However, this is not required for the assignment, and is fairly easy to implement.

#1: Get user location through console input or mouse click
    

#2: Calculates the distance between two points
def distance_a_b(a, b):
    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return round(distance)

#3: Takes user location, Food Location Dictionary, and returns Dictionary with sorted distances for iteration.         
def sort_distance(user_location, canteens_location):
    distance_list = []
    for key,value in canteens_location.items():
        distance_list.append([key, distance_a_b(user_location, (value["Coordinates"][0]))])
    
    #sort distance list
    for passnum in range(len(distance_list)-1):
        swapped = False
        for i in range(len(distance_list) - 1 - passnum):
            if distance_list[i][1] > distance_list[i+1][1]:
                temp = distance_list[i]
                distance_list[i] = distance_list[i+1]
                distance_list[i+1] = temp
                swapped = True
        if not swapped:
            break
    return distance_list

#4. Search all Canteens to return the Canteens with Wanted Food.
def search_by_food(foodname, foodlist_canteens):
    food_available_at = []
    for overall in foodlist_canteens.items():
        for food_list in overall[1].items():
            if food_list[0] == "Food" and foodname.lower().capitalize() in food_list[1]:
                food_available_at.append(overall[0])
    return food_available_at

#5. Display the canteens by rank.
def sort_by_rank(ranklist_canteens):
    rank_list = []
    
    #Get Name, Votes, Details
    for restaurant in ranklist_canteens.values():   
        rank_list.append((restaurant[0], restaurant[1]['Votes'], restaurant))
    #Bubblesort the List
    for passnum in range(len(rank_list) - 1):
        swapped = False
        for i in range(len(rank_list) - 1 - passnum):
            if rank_list[i][1] < rank_list[i+1][1]:
                temp = rank_list[i]
                rank_list[i] = rank_list[i+1]
                rank_list[i+1] = temp
                swapped = True
        if not swapped:
            break
    #Edit the Dictionary, Format: Dictionary[1] = List[0]
    for rank_no in range(len(rank_list)):
        ranklist_canteens[rank_no+1] = rank_list[rank_no][2]
    #For easy display
    display_list = []
    for name in rank_list:
        display_list.append(name[0])
    return display_list

#sort_by_rank(rank)
#6. Search all Canteens to display the food within the searched range.
def search_by_price(price, foodlist_canteens):
    price_available_at = []
    for overall in foodlist_canteens.items():
        for food_list in overall[1].items():
            if food_list[0] == "Price Range":                
                if food_list[1][0] <= int(price) <= food_list[1][1]:
                    price_available_at.append(overall[0])
    return price_available_at
    
#7. Return Coordinate of Mouseclick
def mouseclick():
    return pygame.mouse.get_pos()

#8. Text Box


def update_UI():  # update ui portion only
    pygame.display.update((1221, 0, 400, 1221))


# =============================================================================
# def display_UI(screen):
#     pygame.draw.rect(screen, (255, 255, 255), (1221 + 50, 50, 300, 50))  # draw rectangle
#     display_Text(screen, "Search by?", (1221 + 50, 50))
# 
# 
# def display_Canteens(screen, canteens):
#     for i in range(len(canteens)):
#         display_Text(screen, str(i + 1) + "." + canteens[i][0], (1231, 150 + i * 50), 20)
# =============================================================================


def display_map():    
    screen.fill((200,200,200))
    screen.blit(introScreenImage,(0,0))   
    pygame.display.flip()
    return screen
            
            
def get_str():
  while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
      return event.key
    else:
      pass
  
def text(screen, question):
  pygame.font.init()
  current_string = []
  display_textbox(screen, question + ": " + "".join(current_string))
  while True:
    string = ""
    inkey = get_str()
    if inkey == pygame.K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == pygame.K_RETURN:
      break
    elif inkey == pygame.K_MINUS:
      current_string.append("-")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_map()
    display_textbox(screen, "location:")
    display_textbox(screen, question + ": " + "".join(current_string))
    count = 0
    for i in current_string:
        i.lower()
        string += i
    for j in NTU_Food:
        k = j.lower()
        if string in k:
            count += 1
            display_subtab(screen,j,count)   
    if not current_string:
        display_map()
        display_textbox(screen, "location:")
    display_subtab(screen,j,count)
  return "".join(current_string)

def main():
    return(text(screen,"location"))


#Initialize Code
pygame.init()
pygame.display.set_caption("FindingNTUFood")

introScreenImage = pygame.image.load("NTU map.png")
screen = pygame.display.set_mode((1200, 600))

events = pygame.event.get()

    
x = 930
y = 50
width = 235
height = 30
mouse_x = pygame.mouse.get_pos()[0]
mouse_y = pygame.mouse.get_pos()[1]
mouse_pos = pygame.mouse.get_pos()

def display_backbox():
    xba = 930
    yba = 450
    widthba = 235
    heightba = 30
    
    fontobject = pygame.font.Font(None,22)
    pygame.draw.rect(screen, (0,0,0),(xba,yba,widthba,heightba), 0)
    pygame.draw.rect(screen, (255,255,255),(xba,yba,widthba,heightba), 1)
    screen.blit(fontobject.render("back", 1, (255,255,255)),((xba+(widthba/6)),(yba+(heightba/5))))
    pygame.display.flip()

def refresh():
    screen.fill((200, 200, 200))
    screen.blit(pygame.image.load("NTU map.png"), (0,0))

def display_textbox(screen,message):
    x = 930
    y = 50
    widtht = 235
    heightt = 30
    fontobject = pygame.font.Font(None,22)
    pygame.draw.rect(screen, (0,0,0),(x,y,widtht,heightt), 0)
    pygame.draw.rect(screen, (255,255,255),(x,y,widtht,heightt), 1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,255,255)),((x+(widtht/10)),(y+(heightt/4))))
    pygame.display.flip()

def display_rank():
    widthb = 100
    heightb = 40
    x2b = 1060
    y2b = 100
    
    fontobject = pygame.font.Font(None,22)
    pygame.draw.rect(screen, (0,0,0),(x2b,y2b,widthb,heightb), 0)
    pygame.draw.rect(screen, (255,255,255),(x2b,y2b,widthb,heightb), 1)
    screen.blit(fontobject.render("Rank", 1, (255,255,255)),((x2b+(widthb/6)),(y2b+(heightb/5))))
    pygame.display.flip()
    
def display_rank_blue():
    widthb = 100
    heightb = 40
    x2b = 1060
    y2b = 100
    
    fontobject = pygame.font.Font(None,22)
    pygame.draw.rect(screen, (0,0,255),(x2b,y2b,widthb,heightb), 0)
    pygame.draw.rect(screen, (255,255,255),(x2b,y2b,widthb,heightb), 1)
    screen.blit(fontobject.render("Rank", 1, (255,255,255)),((x2b+(widthb/6)),(y2b+(heightb/5))))
    pygame.display.flip()
    
def display_distance():
    x1b = 940
    y1b = 100
    widthb = 100
    heightb = 40
    
    fontobject = pygame.font.Font(None,22)
    pygame.draw.rect(screen, (0,0,0),(x1b,y1b,widthb,heightb), 0)
    pygame.draw.rect(screen, (255,255,255),(x1b,y1b,widthb,heightb), 1)
    screen.blit(fontobject.render("Distance", 1, (255,255,255)),((x1b+(widthb/6)),(y1b+(heightb/5))))
    pygame.display.flip()
    
def display_distance_blue():
    x1b = 940
    y1b = 100
    widthb = 100
    heightb = 40
    
    fontobject = pygame.font.Font(None,22)
    pygame.draw.rect(screen, (0,0,255),(x1b,y1b,widthb,heightb), 0)
    pygame.draw.rect(screen, (255,255,255),(x1b,y1b,widthb,heightb), 1)
    screen.blit(fontobject.render("Distance", 1, (255,255,255)),((x1b+(widthb/6)),(y1b+(heightb/5))))
    pygame.display.flip()
    

def display_box(screen, message):
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),(x,y,width,height), 0)
  pygame.draw.rect(screen, (255,255,255),(x,y,width,height), 1)
  if len(message) != 0:
      screen.blit(fontobject.render(message, 1, (255,255,255)),((x+(width/6)),(y+(height/5))))
  pygame.display.flip()

def display_subtab(screen,message,no):
    fontobject = pygame.font.Font(None,20)
    pygame.draw.rect(screen, (200,200,200),(x,y+(height*no),width,height),0)
    pygame.draw.rect(screen, (0,0,0),(x,y+(height*no),width,height),1)
    screen.blit(fontobject.render(message, 1,(255,0,0)),((x+(width/10)),(y+(height*no)+(height/4))))
    pygame.display.flip()
    
def words(screen,message,no):
    fontobject = pygame.font.Font(None,22)
    screen.blit(fontobject.render(message, 1,(0,0,0)),((x+(width/20)),(y2b+20+(height*no)+(height/4))))
    pygame.display.flip()



display_map()
run = True
while run:
    
    events = pygame.event.get()
    
    xt = 930
    yt = 50
    widtht = 235
    heightt = 30
    x1b = 940
    y1b = 100
    widthb = 100
    heightb = 40
    x2b = 1060
    y2b = 100
    xba = 930
    yba = 450
    widthba = 235
    heightba = 30
    count = 0
    
    mouse_pos = mouseclick()
    mouse_x, mouse_y = mouseclick()
    display_textbox(screen,"Enter a Food/Price/Canteen:")
   
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_pos)
            if xt<mouse_x<xt+widtht and yt<mouse_y<yt+heightt: #textbox
                user = main()
                print(user)
               
                try:
                    user = int(user)
                    print(search_by_price(user, NTU_Food))
                    list_price = search_by_price(user, NTU_Food)
                    display_map()
                    display_textbox(screen,"Enter a Food/Price/Canteen:")
                    for k in list_price:
                        count += 1
                        words(screen,k,count)

                
                except ValueError:
                    user_input = user.lower().capitalize()
                    if user_input in list_of_food:
                        print(search_by_food(user_input, NTU_Food))#returns a list of canteens with the searched food
                        list_canteens = search_by_food(user_input, NTU_Food)
                        display_map()
                        display_textbox(screen,"Enter a Food/Price/Canteen:")
                        for i in list_canteens:
                            count += 1
                            words(screen,i,count)
                            
                
                    else:
                        for i in NTU_Food.keys():
                            if i.lower().capitalize() == user_input.lower().capitalize():
                                print(NTU_Food[i]['Food'])#returns a list of food from that canteen
                                list_food = NTU_Food[i]['Food']
                                display_map()
                                display_textbox(screen,"Enter a Food/Price/Canteen:")
                                for j in list_food:
                                    count += 1
                                    words(screen,j,count)
                                break
                        else:
                            display_map()
                            display_textbox(screen,"Enter a Food/Price/Canteen:")
                            words(screen,"Sorry, no matches were found.",1)
                # All print statements --> display text
                                
            elif 45<mouse_x<855 and 0<mouse_y<600:#click on map
                current_loc = mouse_pos
                display_map()
                display_textbox(screen,"Enter a Food/Price/Canteen:")
                display_rank()
                display_distance_blue()
                display_backbox()
                list_distance = sort_distance(mouse_pos,NTU_Food)
                for m in list_distance[0:10]:
                    count += 1
                    words(screen,(str(m[0]) + ": " + str(m[1]) + "m"),count)
                
            elif xba<mouse_x<xba+widthba and yba<mouse_y<yba+heightba: #backbutton
                display_map()
                display_textbox(screen,"where are you going?")
                
            elif x2b<mouse_x<x2b+widthb and y2b<mouse_y<y2b+heightb: #click on rank tab
                list_rank = sort_by_rank(rank)
                display_map()
                display_textbox(screen,"Enter a Food/Price/Canteen:")
                display_backbox()
                display_distance()
                display_rank_blue()
                for n in list_rank:
                    count += 1
                    words(screen,n,count)
                    
            elif x1b<mouse_x<x1b+widthb and y1b<mouse_y<y1b+heightb: #click on distance tab
                display_map()
                display_textbox(screen,"Enter a Food/Price/Canteen:")
                display_backbox()
                display_distance_blue()
                display_rank()
                for m in list_distance[0:10]:
                    count += 1
                    words(screen,(str(m[0]) + ": " + str(m[1]) + "m"),count)
                
            
                
        
# =============================================================================
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 display_buttons()
#             if event.key == pygame.K_DOWN:
#                 display_backbox()
# 
# =============================================================================










pygame.quit()