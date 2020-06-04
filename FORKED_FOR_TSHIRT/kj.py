#!/usr/bin/env python
# coding: utf-8

# In[1]:


def win(p,total):
    print(total)
    if (total[0]==total[1] and total[0]==total[2] and total[0]==p) or (total[3]==total[4] and total[3]==total[5] and total[3]==p) or (total[6]==total[7] and total[6]==total[8] and total[6]==p) or (total[0]==total[4] and total[0]==total[7] and total[0]==p) or (total[4]==total[8] and total[4]==total[2] and total[4]==p):
        return True
    else:
        return False


# In[2]:


def grid(total):
    print("{}|{}|{}".format(total[0],total[1],total[2]))
    print("{}|{}|{}".format(total[3],total[4],total[5]))
    print("{}|{}|{}".format(total[6],total[7],total[8]))
#grid()                                           


# In[3]:


def main_game(): 
    player2 = "l"
    player1= input("enter your symbol- X/0--> ")
    if player1 == "X":
        player2 = "0"
    elif player1== "0":
        player2 = "X"
    else:
        player1= input("enter your symbol- X/0--> ")  
    print("player1 = " + player1 + " player2 = " + player2)
    #game here
    
    no_winner = True
    total = [1,2,3,4,5,6,7,8,9]
    grid(total)
    while no_winner:
        
        total[int(input("player1 -> enter position "))-1] = player1
        grid(total)
        if win(player1,total):
            print("player1 won")
            status =False
            break
        total[int(input("player2 -> enter position "))-1] = player2
        grid(total)
        if win(player2,total):
            print("player1 won")
            status =False
            break


# In[4]:


def ask_replay():
    reply = input("do you want to play again - y/n")
    if reply == "y":
        print("thanks for playing again")
        play()
    else:
        print(" quitting the game")


# In[ ]:


def play():
    
    main_game()
    ask_replay()
    


# In[ ]:


play()


# In[ ]:





# In[ ]:





# In[ ]:




