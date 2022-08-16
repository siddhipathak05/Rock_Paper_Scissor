#!/usr/bin/env python
# coding: utf-8

# # Project1   Rock, Paper, Scissor Game

# In[1]:


def Result(YouWin,ComputerWin):
    if (YouWin > ComputerWin):
        print("                                ****    You Win the Game    ****\n")

    elif (ComputerWin > YouWin):
        print("                               ****     You Loss, Computer Win the Game    ****          \n")

    else:
        print("                               ****    Match DRAW     ****\n")

def ScoreKeeper(YouWin,ComputerWin,DrawMatch):
    print("Score is :\n","Your Score : ",YouWin," Computer Score : ",ComputerWin, " DrawMatch : ",DrawMatch)
import random


# In[2]:


Choice=["Rock","Paper","Scissor"]


# In[3]:


while True:
    print("\n\nRock Paper Scissor Game : \n")
    YouWin=0
    ComputerWin=0
    DrawMatch=0
    for i in range(1,6):
        print("Round ",i," Start :")
        print("Select an option (a, b or c): ")
        print("a. Rock \nb.Paper \nc.Scissor")
        YourChoice=input()
        if YourChoice=="a":
            print("You select Rock")
            YourChoice="Rock"
        elif YourChoice=="b":
            print("You select Paper")
            YourChoice="Paper"
        elif YourChoice=="c":
            print("You select Scissor")
            YourChoice="Scissor"
        else:
            print("Invalid Choice.")
            break
        ComputerChoice=random.choice(Choice)
        print("Computer select ",ComputerChoice,"\n")
        
        if (YourChoice==ComputerChoice):
            print("**    DRAW    **\n")
            DrawMatch+=1
        elif (YourChoice=="Paper" and ComputerChoice=="Scissor") or (YourChoice=="Scissor" and ComputerChoice=="Rock") or (YourChoice=="Rock" and ComputerChoice=="Paper") :
            ComputerWin+=1
            print("** Computer win this round **\n")
        else:
            YouWin+=1
            print("** You win this round **\n")
    Result(YouWin,ComputerWin)  
    ScoreKeeper(YouWin,ComputerWin,DrawMatch)
    
    UserChoice=input("\nWant to play again? (Press 1 to continue) : ")
    if (UserChoice=="1"):
        continue
    else:
        break

