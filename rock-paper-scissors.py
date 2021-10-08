import random,os

bot = random.choice(['rock','paper','scissors'])
player= input("rock paper scissors?\nplayer : ")

while player not in ['rock','paper','scissors'] :
    print("error!")
    os.system('clear')
    player= input("rock paper scissors?\nplayer : ")

print("bot : ",bot)
if player == bot :
    print("draw")
elif player == "rock" and bot == 'paper' :
    print("you lost!")
elif player == "rock" and bot == "scissors":
    print("you win")

elif player == "paper" and bot == "rock" :
    print("you win!")
elif player == "paper" and bot == "scissors":
    print("you lost")

elif player == "scissors" and bot == 'paper' :
    print ("you win!")
elif player == "scissors" and bot == "rock":
    print ("you lost")