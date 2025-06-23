import random
import json
import time
import os

class game:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.wins = 0

    def play(self):
        print(f"welcome to {self.name} the game od guessing a number")
        if self.difficulty == "easy":
            print("the game is easy, you have only 10 attempts")
            number_attempts = 10
        elif self.difficulty == "medium":
            print("the game is medium, you have 7 attempts")
            number_attempts = 7
        elif self.difficulty == "hard":
            print("the game is hard you have 5 attempts")
            number_attempts = 5
        else:
            print("please enter a valid difficulty")
        number = random.randint(1, 100)
        player_number = int(input("please enter your number: "))
        attempts = 0
        while player_number != number or attempts < number_attempts + 1:
            if player_number == number:
                print("you win!")
                self.wins += 1
                break
            else:
                print("you lose")
                attempts += 1
                if attempts == number_attempts:
                    print("the game is over, you lost")
                    break
    
class save_score:
    def save():
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as f:
                scores = json.load(f)
                print(scores)
        
                    
        