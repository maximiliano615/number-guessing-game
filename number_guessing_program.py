import random
import json
import time
import os
from errors import errors
from funtions import save_score, system_suggestions, game

print("welcome to the number guessing game")
print("""this game have a 3 difficulty levels
easy = 10 attempts
medium = 7 attempts
hard = 5 attempts
""")

name = input("please enter your name: ")
difficulty = input("please enter the difficulty level: ")
juego = True
while juego == True:
    gaming = game(name, difficulty)
    gaming.play()
    while juego == True:
        desicion = input("do you want to play again? yes or no => ")
        if desicion == "yes":
            print("ok, let's play again")
        elif desicion == "no":
            print("ok, bye")
            juego = False
        else:
            print("please enter yes or no")

