# random is used to choose a character from chars string
import random
from pyfiglet import Figlet
f = Figlet(font='big')
print(f.renderText(' 1. Create \n 2. Saved \n 3. Encode \n 4. Decode '))

option = int(input())

if option == 1:

    # taking input from users about how long password to be they want
    length = int(input("length of password no."))
    c = 3
    # chars variable is used to store all alphabet and numeric values
    chars = "[@_!#$%^&*()<>?/\|}{~:]ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

    for b in range(c):

        # To start with, our password variable should be empty
        password = " "

        # intialize the length as the argument in for loop
        for a in range(length):
            # password variable is used to store a random variable from char string and + is used to add the letter each time
            password += random.choice(chars)

        # it is used print the password variable
        print("\n", password, "\n")
    save = str(input("Do you want to save this password say (YES/NO)"))
    if save == "YES":
        f = open("SAVED_PASSWORD.txt", "a+")
        for i in range(1):
            new = str(input("tag + password"))
            f.write(" \nADDED   %s \r\n" % (str(new)))

        print("THANK YOU, PASSWORD SAVED")

elif option == 2:

    print("Your saved password", )
    text_file = open("SAVED_PASSWORD.txt", "r")
    print(text_file.read(100))


elif option == 3:

    alphabet = "abcdefghijklmnopqrstuvwxyz"


    def number_to_letter(i):
        return alphabet[i % 26]


    def letter_to_number(l):
        return alphabet.find(l)


    def caesar_shift_single_character(l, amount):
        i = letter_to_number(l)
        if i == -1:
            return ""
        else:
            return number_to_letter(i + amount)


    def caesar_shift(text, amount):
        shifted_text = ""
        for char in text.lower():
            shifted_text += caesar_shift_single_character(char, amount)
        return shifted_text


    message = input(str(" enter your message  :    "))

    code = caesar_shift(message, 2)

    print("\n\nYour encoded message  :  ", code, " ")


elif option == 4:
    alphabet = "abcdefghijklmnopqrstuvwxyz"


    def number_to_letter(i):
        return alphabet[i % 26]


    def letter_to_number(l):
        return alphabet.find(l)


    def caesar_shift_single_character(l, amount):
        i = letter_to_number(l)
        if i == -1:
            return ""
        else:
            return number_to_letter(i + amount)


    def caesar_shift(text, amount):
        shifted_text = ""
        for char in text.lower():
            shifted_text += caesar_shift_single_character(char, amount)
        return shifted_text


    message = input(str(" enter your message  :    "))

    code = caesar_shift(message, -2)

    print("\n\nYour encoded message  :  ", code, " ")

else:

    print("invalid input, please try again")
