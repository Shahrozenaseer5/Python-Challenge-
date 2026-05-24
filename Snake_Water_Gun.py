# Snake Water Gun 
# Snake water gun is a variation of the children's game "Rock-Paper-Scissors" where players use hand gestures
# to represent a snake, water or a gun. The gun beats the snake, water beats the gun and snake beats the water.
# Write a python program to create a snake water gun game in python using if-else statements.
# Do not create any fancy GUI. Use proper functions to check for win.
#                  S  W  G
#  computer =      0  1  2
#  Player   = S  0 D  W  L
#             W  1 L  D  W
#             G  2 W  L  D
# ==========================================
#   Project: Snake Water Gun Game
#   Description:
#       A simple two-player "Snake-Water-Gun" game
#       implemented using basic input handling and
#       if-else conditions.
#
#       Rules:
#           • Snake beats Water
#           • Water beats Gun
#           • Gun beats Snake
#
#   Author: Shahroze
#   Date:   24-11-2025
#   Status: Completed
# ==========================================

import os
os.system('cls')
def snake_water_gun(snake, water, gun) :
    if Player_1 == snake and Player_2 == snake :
      print("It's a Draw 🙂")
    elif Player_1 == snake and Player_2 == water :
      print("Player_1 wins 🙂")
    elif Player_1 == snake and Player_2 == gun :
      print("Player_2 wins 🙂")
    elif Player_1 == water and Player_2 == snake :
      print("Player_2 wins 🙂")
    elif Player_1 == water and Player_2 == water :
      print("It's a Draw 🙂")
    elif Player_1 == water and Player_2 == gun :
      print("Player_1 wins 🙂")
    elif Player_1 == gun and Player_2 == snake :
      print("Player_1 wins 🙂")
    elif Player_1 == gun and Player_2 == water :
      print("Player_2 wins 🙂")
    elif Player_1 == gun and Player_2 == gun :
      print("It's a Draw 🙂")
    else : 
      print("Wrong choice _ ")
print('Snake Water Gun...')
Player_1 = input('Player_1 Please select Snake, Water or Gun : ').lower()
Player_2 = input('Player_2 Please select Snake, Water or Gun : ').lower()
print(f"Player_1 choose {Player_1} and Player_2 choose {Player_2}")
print("fighting ...")
snake_water_gun('snake', 'water', 'gun')
