import random
rnum=random.randint(1,10)
unum=int(input("Enter your number:"))
guess=[]

if unum>=1 and unum<=10:
    guess.append(unum)
    while unum != rnum:
        if unum<rnum:
            print("Please try higher value")
        else:
            print("Please try lower value")

        unum=int(input("Enter your number:"))
        guess.append(unum)

    if len(guess)<=5:
        print("You have won!!!")
    else:
        print(f"You have lost. You have tried {len(guess)} Try again")
else:
    print("Restart the game and try with number within 1 to 10")
