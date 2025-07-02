import random
import json
import time
import os

class save_score:
    def save(self,attempts, name):
        if os.path.exists("scores.json"):
            with open("scores.json", "r") as f:
                scores = {"name": name , "attempts": attempts}
                scores_loaded = json.load(f)
                scores = scores | scores_loaded
            with open("scores.json", "w") as f:
                json.dump(scores, f, indent=4)
        else:
            with open("scores.json", "w") as f:
                scores =  {"name": name , "attempts": attempts} 
                json.dump(scores, f, indent=4)

    def load ():
        with open(scores.json, "r") as f:
            scores = json.load(f)
            print(scores)

class system_suggestions:
    def suggestions(self, number, player_number):
        if player_number > number and player_number-number > 10:
            print("your number is too high")
        elif player_number > number and player_number-number <= 10:
            print("your number is high but is near")
        elif player_number < number and number-player_number > 10:
            print("your number is too low")
        elif player_number < number and number-player_number <= 10:
            print("your number is low but is near")

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
        attempts = 0
        start_time = time.time()
        while attempts < number_attempts + 1:
            suggest = number_attempts - attempts
            if suggest < 3:
                print(f"you have only {suggest} attempts left, want a hint? yes or not => ")
                decition = input("want a hint? yes or not => ")
                if decition == "yes":
                    system_suggestions().suggestions(number, player_number)
                    print(number)
                elif decition == "not":
                    print("ok, let's play again")
                else:
                    print("please enter yes or no")
            player_number = int(input("please enter your number: "))
             
            if player_number == number:
                self.wins += 1
                final_time = time.time()
                print("you win!")
                print(f"you won in {final_time - start_time} seconds")
                save_score().save(attempts, self.name)
                break
            else:
                print("you lose")
                attempts += 1
                if attempts == number_attempts:
                    print("the game is over, you lost")
                    break


primer = game("jose", "medium")
primer.play()

        
                    
        