# Buggy and incomplete
# But still works 40% of the time, somehow

import random

possibleLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


confirmedLetters = {}
commonLetters = ["cbtpaf", "aoreiluh", "aioeurn", "ensalircto", "eytrlhnd"]

dictionary = open("dictionary.txt", "r").readlines()
for wordIndex in range(len(dictionary)):
    dictionary[wordIndex] = dictionary[wordIndex].strip()

def check(guess):
    global confirmedLetters
    print(guess)
    result = input()
    for letterIndex in range(5):
        guessedLetter = guess[letterIndex]
        resultLetter = result[letterIndex]
        if resultLetter == "+":
            pass
        elif resultLetter == "*":
            if not guessedLetter in confirmedLetters.keys():
                confirmedLetters[guessedLetter] = {
                    "placed": False,
                    "indexes": [letterIndex]
                }
            elif not confirmedLetters[guessedLetter]["placed"] and not letterIndex in confirmedLetters[guessedLetter]["indexes"]:
                confirmedLetters[guessedLetter]["indexes"].append(letterIndex)
        else:
            if not guessedLetter in confirmedLetters.keys() or not confirmedLetters[guessedLetter]["placed"]:
                confirmedLetters[guessedLetter] = {
                    "placed": True,
                    "indexes": [letterIndex]
                }
            elif not letterIndex in confirmedLetters[guessedLetter]["indexes"]:
                confirmedLetters[guessedLetter]["indexes"].append(letterIndex)

for i in range(5):
    check(dictionary[random.randint(0, len(dictionary))])

possibleWords = []

for word in dictionary:
    possibility = True
    for confirmedLetter, info in confirmedLetters.items():
        if confirmedLetter in word:
            for index in info["indexes"]:
                if word[index] == confirmedLetter != info["placed"]:
                    possiblity = False
        else:
            possibility = False
    if possibility:
        possibleWords.append(word)

print(possibleWords)
print(len(possibleWords))