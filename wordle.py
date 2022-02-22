import random

commonLetters = ["cbtpaf", "aoreiluh", "aioeurn", "ensalircto", "eytrlhnd"]

dictionary = open("dictionary.txt", "r").readlines()
for wordIndex in range(len(dictionary)):
    dictionary[wordIndex] = dictionary[wordIndex].strip()

def check(guess, word):
    result = ""
    for letterIndex in range(len(guess)):
        guessedLetter = guess[letterIndex]
        wordLetter = word[letterIndex]
        if guessedLetter == wordLetter:
            result += guessedLetter
        elif guessedLetter in word:
            result += "*"
        else:
            result += "+"
    return result

class Wordle:
    def __init__(self):
        self.confirmedLetters = {}
        self.possibleWords = []
        self.guessNumber = 0
    def check(self, guess, result):
        self.guessNumber += 1
        for letterIndex in range(5):
            guessedLetter = guess[letterIndex]
            resultLetter = result[letterIndex]
            if resultLetter == "+":
                pass
            elif resultLetter == "*":
                if not guessedLetter in self.confirmedLetters.keys():
                    self.confirmedLetters[guessedLetter] = {
                        "placed": False,
                        "indexes": [letterIndex]
                    }
                elif not self.confirmedLetters[guessedLetter]["placed"] and not letterIndex in self.confirmedLetters[guessedLetter]["indexes"]:
                    self.confirmedLetters[guessedLetter]["indexes"].append(letterIndex)
            else:
                if not guessedLetter in self.confirmedLetters.keys() or not self.confirmedLetters[guessedLetter]["placed"]:
                    self.confirmedLetters[guessedLetter] = {
                        "placed": True,
                        "indexes": [letterIndex]
                    }
                elif not letterIndex in self.confirmedLetters[guessedLetter]["indexes"]:
                    self.confirmedLetters[guessedLetter]["indexes"].append(letterIndex)
    def nextGuess(self):
        self.updatePossibleWords()
        if self.guessNumber == 0:
            return "crane"
        else:
            return self.possibleWords[random.randint(0, len(self.possibleWords) - 1)]
    def updatePossibleWords(self):
        self.possibleWords = []
        for word in dictionary:
            possibility = True
            for confirmedLetter, info in self.confirmedLetters.items():
                if confirmedLetter in word:
                    for index in info["indexes"]:
                        if (word[index] == confirmedLetter) != info["placed"]:
                            possibility = False
                            break
                else:
                    possibility = False
                    break
            if possibility:
                self.possibleWords.append(word)
    def isCorrect(self, word):
        possibilities = len(self.possibleWords)
        return possibilities == 1 and self.possibleWords[0] == word

correct = 0
tests = 5000
for i in range(tests):
    word = dictionary[random.randint(0, len(dictionary) - 1)]
    wordle = Wordle()
    for j in range(5):
        guess = wordle.nextGuess()
        wordle.check(guess, check(guess, word))
    wordle.updatePossibleWords()
    if wordle.isCorrect(word):
        correct += 1

print(str(correct) + "/" + str(tests) + " = " + str(round(correct / tests, 2) * 100) + "%")