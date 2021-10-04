import json
from random import choice

def newSequence(char, word, NewWord):
    indices = [i for i,j in enumerate(word) if j==char]
    sequence = [letter for letter in NewWord]
    for i in indices:
        sequence[i] = char
    return "".join(sequence)

def getLevel():
    while 1:
        level = input()
        try:
            level = int(level)
            if not 1<=level<=3:
                print("Enter number is the proper range")
            else:
                break
        except:
            print("Enter numbers")
    return level

def getChoice():
    while 1:
        cont = input("Want to continue? (y or n)").lower()
        if cont=='y' or cont=='n':
            return cont
        else:
            print("Enter either 'y' or 'n'")

def game(chances, word):
    print(f"You have {chances} chances to guess the word correctly")
    print("Word:", end=" ")
    print("-"*len(word))
    guess = input("Enter character: ")
    chance = 0

    NewWord = "-"*len(word)
    while True:
        print()
        print("="*20)
        print()
        if len(guess) == 1:
            if guess in word:
                NewWord = newSequence(guess, word, NewWord)
                print("Word:", NewWord)
                if NewWord == word:
                    print("You guessed the correct word!!")
                    break
            else:
                print('your guess is wrong')
                print("Word:", NewWord)
                chance+=1
                if chance==chances:
                    print("You lost")
                    print("Word was:", word)
                    break
                print("Remaining chances: ",chances-chance)
            guess = input("Enter next character: ")
        else:
            print("Enter only one character")
            guess = input("Enter character: ")

cont = 'y'
while cont=='y':
    jsonFile = open('hangman\words.json')
    word_list = json.load(jsonFile)

    print("Enter difficulty level (1-3)")
    print("1 - Easy\n2 - Normal\n3 - Difficult")

    level = getLevel()

    print("Level is set to", level)

    if level==1:
        word_list = [words for words in word_list["data"] if len(words)<6]
        word = choice(word_list)
        game(5, word)
    elif level==2:
        word_list = [words for words in word_list["data"] if 6<=len(words)<=8]
        word = choice(word_list)
        game(3, word)
    else:
        word_list = [words for words in word_list["data"] if len(words)>8]
        word = choice(word_list)
        game(3, word)
    cont = getChoice()
    jsonFile.close()