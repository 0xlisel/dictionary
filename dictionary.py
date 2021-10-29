# Word Dictionary program in python
import json
from difflib import get_close_matches
import time

def decision(content, word):
    decision = input("Enter (y) Yes or (n) No: ")

    if decision.lower() == "y":
        return content[get_close_matches(word, content.keys())[0]]

    elif decision.lower() == "n":
        return "Word not found!"

    else:
        return "Invalid Input! \nEnter (y) Yes or (n) No: "


def search(word):
    with open("data.json") as data:

        content = json.load(data)
        if word.lower in content:
            return content[word.lower()]

        elif len(get_close_matches(word, content.keys())) > 0:
            print("\nHmmm.....")
            time.sleep(1)
            print("Did you mean %s instead?" %(get_close_matches(word, content.keys())[0]))
        
            return decision(content, word)

        else:
            return("Word not found!")
            

word = input("Enter the word you want to search: ")
output = search(word)
print("\n-> " + output)