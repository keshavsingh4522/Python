# Rock paper game
import random

my_win = 0
my_loss = 0
my_tie = 0


def game():

    global my_tie, my_loss, my_win

    var = {"scissors": (0, 1, 0), "paper": (0, 0, 1), "rock": (1, 0, 0)}

    user = input("Please choice scissors, paper or rock: ")
    while user not in ["scissors", "paper", "rock"]:
        user = input("Please choice scissors, paper or rock: ")
    computer = random.choice(["scissors", "paper", "rock"])

    print(f"USER - {user} \nCOMPUTER - {computer}")

    for k, v in var.items():
        if k == user:
            one = int(v.index(1))
        if k == computer:
            two = int(v.index(1))

    if one < two:
        print(f"USER with {user} - WIN!")
        my_win += 1
    elif one == two:
        print("==TIE==")
        my_tie += 1
    else:
        print(f"COMPUTER with {computer} - WIN!")
        my_loss += 1

    def results():

        print("You win %d times!" % my_win)
        print("You lose %d times!" % my_loss)
        print("You tie %d times!" % my_tie)


if __name__ == "__main__":
    game()
