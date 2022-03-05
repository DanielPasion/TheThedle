from WordDatabase import *
import random


#Picking a random word
electedWord = random.choice(listOfWords)
electedArray = ['f','i','n','g','e','r']
#for i in electedWord:
    #electedArray.append(i)
#Method for checking if the wordle is correct
def checkAnswer(list,trial):
    
    #Case 1: the answer is correct
    if electedArray[0] == list[0] and electedArray[1] == list[1] and electedArray[2] == list[2] and electedArray[3] == list[3] and electedArray[4] == list[4] and electedArray[5] == list[5]:
        print (trial + ": " + ["green","green","green","green","green","green"])
        print ("dubs")



#thethedle
print("Welcome to TheThedle!")



#first guess

#Getting user input and turning it into a string of characters
guessOne = input("Enter Word: ")
while (len(guessOne) != 6):
    guessOne = input("Enter Word: ")
oneArray = []
for i in guessOne:
    oneArray.append(i)
checkAnswer(oneArray,1)
