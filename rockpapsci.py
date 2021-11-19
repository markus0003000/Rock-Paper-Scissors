#Import libraries
import random

#Set choices for the game
choices = ['rock','paper','scissors']

#Have user enter their choice of rock, paper, scissors
reply = str(input('Rock, paper, or scissors? ')).lower().strip()
while reply not in choices:
    reply = str(input('Rock, paper, or scissors? ')).lower().strip()

#Get random computer selection of rock, paper, or scissors
comp_reply = random.choice(choices)
print("Computer plays {}".format(comp_reply))

#Check to see who won
if reply == comp_reply:
    print("It's a tie! Computer played {} and so did you.".format(reply))
elif (reply == 'rock' and comp_reply == 'scissors') \
     or (reply == 'scissors' and comp_reply == 'paper') \
     or (reply == 'paper' and comp_reply == 'rock'):
    print("You've won, {} beats {}".format(reply,comp_reply))
else:
    print("Sorry, you've lost... {} beats {}".format(comp_reply,reply))
