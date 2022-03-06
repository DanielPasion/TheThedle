from WordDatabase import *
import random


#Picking a random word/useful variables
electedWord = random.choice(listOfWords).lower()
electedArray = []
winGame = False
for i in electedWord:
    electedArray.append(i)




#Methods

#checkAnswer: checks how close the user's guess is to the original word
#parameters: list=user's choice(array) trial:the attempt the user is on (integer)    
def checkAnswer(list,trial):
    
    #Case 1: the answer is correct
    if electedArray[0] == list[0] and electedArray[1] == list[1] and electedArray[2] == list[2] and electedArray[3] == list[3] and electedArray[4] == list[4] and electedArray[5] == list[5]:
        print (str(trial) + ": " + str(["green","green","green","green","green","green"]))
        print ("dubs")
        winGame = True
        quit()     
    
    #Case anything else:
    print (str(trial) + ": " + str([determineColor(list,0),determineColor(list,1),determineColor(list,2),determineColor(list,3),determineColor(list,4),determineColor(list,5)]))    
        
              
#toArray: returns the user's string input to an array of each individual character
#parameters: string=the input from the user (string)
def toArray(string):
    array = []
    for i in string:
        array.append(i)
    return array   



#determineColor: determines how close the indicated letter is
#paramaters: list=the user's selection in array format(array) int=which letter in the word you are checking for starting at 0, ending at 5(int)
def determineColor(list,int):
    if (electedArray[int] != list[int] and electedArray[0] != list[int] and electedArray[1] != list[int] and electedArray[2] != list[int] and electedArray[3] != list[int] and electedArray[4] != list[int] and electedArray[5] != list[int]):
        return "black"
    elif (electedArray[int] != list[int]) and (electedArray[0] == list[int] or electedArray[1] == list[int] or electedArray[2] == list[int] or electedArray[3] == list[int] or electedArray[4] == list[int] or electedArray[5] == list[int]):
        return "yellow"
    elif (electedArray[int] == list[int]):
        return "green"    


















#thethedle
print("Welcome to TheThedle!")



#first guess

#Getting user input and turning it into a string of characters
guessOne = input("Enter Word: ")
oneArray = toArray(guessOne.lower())

#sanitizing
while ((len(oneArray)) != 6) or guessOne.isalpha() == False:
    guessOne = input("Enter Word: ")
    oneArray = toArray(guessOne)
#checking if the answer is correct
checkAnswer(oneArray,1)


#second guess

#Getting user input and turning it into a string of characters
guessTwo = input("Enter Word: ")
twoArray = toArray(guessTwo.lower())

#sanitizing
while ((len(oneArray)) != 6) or guessOne.isalpha() == False:
    guessTwo = input("Enter Word: ")
    twoArray = toArray(guessTwo)
#checking if the answer is correct
checkAnswer(twoArray,2)


#third guess

#Getting user input and turning it into a string of characters
guessThree = input("Enter Word: ")
threeArray = toArray(guessThree.lower())

#sanitizing
while ((len(oneArray)) != 6) or guessOne.isalpha() == False:
    guessThree = input("Enter Word: ")
    threeArray = toArray(guessThree)
#checking if the answer is correct
checkAnswer(threeArray,3)


#forth guess

#Getting user input and turning it into a string of characters
guessFour = input("Enter Word: ")
fourArray = toArray(guessFour.lower())

#sanitizing
while ((len(oneArray)) != 6) or guessOne.isalpha() == False:
    guessFour = input("Enter Word: ")
    fourArray = toArray(guessFour)
#checking if the answer is correct
checkAnswer(fourArray,4)


#fifth guess

#Getting user input and turning it into a string of characters
guessFive = input("Enter Word: ")
fiveArray = toArray(guessFive.lower())

#sanitizing
while ((len(oneArray)) != 6) or guessOne.isalpha() == False:
    guessFive = input("Enter Word: ")
    fiveArray = toArray(guessFive)
#checking if the answer is correct
checkAnswer(fiveArray,5)


if (winGame == False):
    print ("L bozo")
    print("The word was " + electedWord)