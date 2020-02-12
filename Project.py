import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Enter a word: ")

try:
    def translate(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        else:
            pred = get_close_matches(word, data.keys())[0]
            YoN = input("Did you mean '" + str(pred) + "'? [Y/N]: ")
            YoN = YoN.upper()
            if YoN == "Y":
                return data[pred]
            elif YoN == "N":
                return "The word '" + word + "' does not exist. Please check again."
            else:
                return "Invalid Entry!"

    output = (translate(word))

    if (type(output) == list):
        for item in output:
            print(item)
    else:
        print(output)

except KeyError:
    print("The word '" + word + "' does not exist. Please check again.")

except IndexError:
    print("The word '" + word + "' does not exist. Please check again.")
