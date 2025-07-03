
import json
import os

class errors:
    def errors_with_int(self, number):
        try:
            int(number)
            return(True)
        except ValueError:
            print("please enter a valid number")
            return(False)

    def errors_with_save(self):
        try:
            if os.path.exists("scores.json"):
                with open("scores.json", "r") as f:
                    scores = json.load(f)
                    print(scores)
            else:
                print("the game has not been saved")
        except:
            data = []
            with open("scores.json", "w") as f:
                json.dump(data, f, indent=4)