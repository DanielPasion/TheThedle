import tkinter as tk
from tkinter import *
from WordDatabase import *
import random

#Vairables
HEIGHT = 800
WIDTH = 800
electedWord = random.choice(listOfWords).upper()
electedArray = []


#Putting each letter of the correct word into an array
for i in electedWord:
    electedArray.append(i)
print(electedWord)


#Creating the main window
root = tk.Tk()


#Setting up the canvas for the application
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background = tk.Frame(root,bg="black")
background.place(relx=.1,rely=.1,relwidth=.8,relheight=.8)
root.resizable(0,0) #makes program unresizeable












#Useful Functions

#setWord*****: takes the user's guess and turns it into a string, where each index is displayed onto the box. Also sanitizes the data
#for word one
def setWordOne(guessOne):
    oneArray = []
    guessOne = sv1.get().upper()
    print (guessOne)
    for i in guessOne:
        oneArray.append(i)
    #case if the word is not acceptable    
    if ((len(oneArray)) != 6) or guessOne.isalpha() == False:
        oneWord.delete(0, "end")
        prompt.configure(text="Invalid entry, please try again")
        return
    prompt.configure(text="One down, four to go!")
    oneWord.destroy()
    twoWord.place(x=100,y=325)
    oneWord1.config(text=oneArray[0])
    oneWord2.config(text=oneArray[1])
    oneWord3.config(text=oneArray[2])
    oneWord4.config(text=oneArray[3])
    oneWord5.config(text=oneArray[4])
    oneWord6.config(text=oneArray[5])
    checkAnswerOne(oneArray)
    

#for word two
def setWordTwo(guessTwo):
    twoArray = []
    guessTwo = sv2.get().upper()
    print (guessTwo)
    for i in guessTwo:
        twoArray.append(i)
    #case if the word is not acceptable    
    if ((len(twoArray)) != 6) or guessTwo.isalpha() == False:
        twoWord.delete(0, "end")
        prompt.configure(text="Invalid entry, please try again")
        return
    prompt.configure(text="Two down, three to go!")
    twoWord.destroy()
    threeWord.place(x=100,y=400)
    twoWord1.config(text=twoArray[0])
    twoWord2.config(text=twoArray[1])
    twoWord3.config(text=twoArray[2])
    twoWord4.config(text=twoArray[3])
    twoWord5.config(text=twoArray[4])
    twoWord6.config(text=twoArray[5])
    checkAnswerTwo(twoArray)
    
#for word three
def setWordThree(guessThree):
    threeArray = []
    guessThree = sv3.get().upper()
    print (guessThree)
    for i in guessThree:
        threeArray.append(i)
    #case if the word is not acceptable    
    if ((len(threeArray)) != 6) or guessThree.isalpha() == False:
        threeWord.delete(0, "end")
        prompt.configure(text="Invalid entry, please try again")
        return
    prompt.configure(text="Three down, two to go!")
    threeWord.destroy()
    fourWord.place(x=100,y=475)
    threeWord1.config(text=threeArray[0])
    threeWord2.config(text=threeArray[1])
    threeWord3.config(text=threeArray[2])
    threeWord4.config(text=threeArray[3])
    threeWord5.config(text=threeArray[4])
    threeWord6.config(text=threeArray[5])  
    checkAnswerThree(threeArray)
    
#for word four
def setWordFour(guessFour):
    fourArray = []
    guessFour = sv4.get().upper()
    print (guessFour)
    for i in guessFour:
        fourArray.append(i)
    #case if the word is not acceptable    
    if ((len(fourArray)) != 6) or guessFour.isalpha() == False:
        fourWord.delete(0, "end")
        prompt.configure(text="Invalid entry, please try again")
        return
    prompt.configure(text="Last Chance!!!!")
    fourWord.destroy()
    fiveWord.place(x=100,y=550)
    fourWord1.config(text=fourArray[0])
    fourWord2.config(text=fourArray[1])
    fourWord3.config(text=fourArray[2])
    fourWord4.config(text=fourArray[3])
    fourWord5.config(text=fourArray[4])
    fourWord6.config(text=fourArray[5])  
    checkAnswerFour(fourArray) 

#for word five
def setWordFive(guessFive):
    fiveArray = []
    guessFive = sv5.get().upper()
    print (guessFive)
    for i in guessFive:
        fiveArray.append(i)
    #case if the word is not acceptable    
    if ((len(fiveArray)) != 6) or guessFive.isalpha() == False:
        fiveWord.delete(0, "end")
        prompt.configure(text="Invalid entry, please try again")
        return
    fiveWord.destroy()
    fiveWord1.config(text=fiveArray[0])
    fiveWord2.config(text=fiveArray[1])
    fiveWord3.config(text=fiveArray[2])
    fiveWord4.config(text=fiveArray[3])
    fiveWord5.config(text=fiveArray[4])
    fiveWord6.config(text=fiveArray[5])  
    checkAnswerFive(fiveArray)        



def determineColor(list):
    color5 = ""
    color4 = ""
    color3 = ""
    color2 = ""
    color1 = ""
    color0 = ""
    
    #last letter
    if(list[5] == electedArray[5]):
        color5 = "green"
        
    if(list[5] != electedArray[5]):
        frequencyOG = 0
        frequencyGuess = 0
        for i in range(6):
            if electedArray[i] == list[5]:
                frequencyOG = frequencyOG + 1
            if list[i] == list[5]:
                frequencyGuess = frequencyGuess + 1
        
        if frequencyGuess > frequencyOG:
            color5 = "gray"
        elif (frequencyGuess <= frequencyOG):
            color5 = "yellow"
    
    
    #fifth letter
    if(list[4] == electedArray[4]):
        color4 = "green"
    elif(list[4] != electedArray[4]):
        frequencyOG = 0
        frequencyGuess = 0
        for i in range(6):
            if electedArray[i] == list[4]:
                frequencyOG = frequencyOG + 1
        for i in range(5):
            if list[i] == list[4]:
                frequencyGuess = frequencyGuess + 1
        
        if (frequencyGuess == 1 and frequencyOG == 1) and (list[5] != electedArray[5]):
            color4 = "yellow"
        elif (frequencyGuess == 2 and frequencyOG == 2) and (list[5] != electedArray[5]):
            color4 = "yellow"
        elif (frequencyGuess == 3 and frequencyOG == 3) and (list[5] != electedArray[5]):
            color4 = "yellow"
        else:       
            if list[4] == electedArray[5] and list[5] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if frequencyGuess > frequencyOG:
                color4 = "gray"
            elif (frequencyGuess <= frequencyOG):
                color4 = "yellow"
    
    
    #fourth letter
    if(list[3] == electedArray[3]):
        color3 = "green"
        
    elif(list[3] != electedArray[3]):
        frequencyOG = 0
        frequencyGuess = 0
        for i in range(6):
            if electedArray[i] == list[3]:
                frequencyOG = frequencyOG + 1
        for i in range(4):
            if list[i] == list[3]:
                frequencyGuess = frequencyGuess + 1
                
        if (frequencyGuess == 1 and frequencyOG == 1) and (list[5] != electedArray[5] or list[4] != electedArray[4]):
            color3 = "yellow"
        elif (frequencyGuess == 2 and frequencyOG == 2) and (list[5] != electedArray[5] or list[4] != electedArray[4]):
            color3 = "yellow"
        elif (frequencyGuess == 3 and frequencyOG == 3) and (list[5] != electedArray[5] or list[4] != electedArray[4]):
            color3 = "yellow"
        else:        
            if list[3] == electedArray[5] and list[5] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if list[3] == electedArray[4] and list[4] == electedArray[4]:
                frequencyOG = frequencyOG - 1 
            if frequencyGuess > frequencyOG:
                color3 = "gray"
            elif (frequencyGuess <= frequencyOG):
                color3 = "yellow"
    
    
    #third letter
    if(list[2] == electedArray[2]):
        color2 = "green"
        
    elif(list[2] != electedArray[2]):
        frequencyOG = 0
        frequencyGuess = 0
        for i in range(6):
            if electedArray[i] == list[2]:
                frequencyOG = frequencyOG + 1
        for i in range(3):
            if list[i] == list[2]:
                frequencyGuess = frequencyGuess + 1
                
        if (frequencyGuess == 1 and frequencyOG == 1) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3]):
            color2 = "yellow"
        elif (frequencyGuess == 2 and frequencyOG == 2) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3]):
            color2 = "yellow"
        elif (frequencyGuess == 3 and frequencyOG == 3) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3]):
            color2 = "yellow"
        else:        
            if list[2] == electedArray[5] and list[5] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if list[2] == electedArray[4] and list[4] == electedArray[4]:
                frequencyOG = frequencyOG - 1
            if list[2] == electedArray[3] and list[3] == electedArray[3]:
                frequencyOG = frequencyOG - 1
            if frequencyGuess > frequencyOG:
                color2 = "gray"
            elif (frequencyGuess <= frequencyOG):
                color2 = "yellow"
            
    
    #second letter
    if(list[1] == electedArray[1]):
        color1 = "green"
        
    elif(list[1] != electedArray[1]):
        frequencyOG = 0
        frequencyGuess = 0
        for i in range(6):
            if electedArray[i] == list[1]:
                frequencyOG = frequencyOG + 1
        for i in range(2):
            if list[i] == list[1]:
                frequencyGuess = frequencyGuess + 1
        
        if (frequencyGuess == 1 and frequencyOG == 1) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3] or list[2] != electedArray[2]):
            color1 = "yellow"
        elif (frequencyGuess == 2 and frequencyOG == 2) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3] or list[2] != electedArray[2]):
            color1 = "yellow"
        elif (frequencyGuess == 3 and frequencyOG == 3) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3] or list[2] != electedArray[2]):
            color1 = "yellow"
        else:        
            if list[1] == electedArray[5] and list[5] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if list[1] == electedArray[4] and list[4] == electedArray[4]:
                frequencyOG = frequencyOG - 1
            if list[1] == electedArray[3] and list[3] == electedArray[3]:
                frequencyOG = frequencyOG - 1
            if list[1] == electedArray[2] and list[2] == electedArray[2]:
                frequencyOG = frequencyOG - 1 
            if frequencyGuess > frequencyOG:
                color1 = "gray"
            elif (frequencyGuess <= frequencyOG):
                color1 = "yellow"
        
    
    #first letter
    if(list[0] == electedArray[0]):
        color0 = "green"
        
    if(list[0] != electedArray[0]):
        frequencyOG = 0
        frequencyGuess = 1
        for i in range(6):
            if electedArray[i] == list[0]:
                frequencyOG = frequencyOG + 1
        
        if (frequencyGuess == 1 and frequencyOG == 1) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3] or list[2] != electedArray[2] or list[1] != electedArray[1]):
            color0 = "yellow"
        elif (frequencyGuess == 2 and frequencyOG == 2) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3] or list[2] != electedArray[2] or list[1] != electedArray[1]):
            color0 = "yellow"
        elif (frequencyGuess == 3 and frequencyOG == 3) and (list[5] != electedArray[5] or list[4] != electedArray[4] or list[3] != electedArray[3] or list[2] != electedArray[2] or list[1] != electedArray[1]):
            color0 = "yellow"
        else:    
            if list[5] == electedArray[5] and list[0] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if list[4] == electedArray[4] and list[0] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if list[3] == electedArray[3] and list[0] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if list[2] == electedArray[2] and list[0] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if list[1] == electedArray[1] and list[0] == electedArray[5]:
                frequencyOG = frequencyOG - 1
            if frequencyGuess > frequencyOG:
                color0 = "gray"
            elif (frequencyGuess <= frequencyOG):
                color0 = "yellow"
            
         

    
    return [color0,color1,color2,color3,color4,color5]
            

            
            
            
            
            
            
            

    
        
        
        
        

    
#Checks the similarities among the chosen word and actual word
def checkAnswerOne(list):
    
    #Case 1: the answer is correct
    if electedArray[0] == list[0] and electedArray[1] == list[1] and electedArray[2] == list[2] and electedArray[3] == list[3] and electedArray[4] == list[4] and electedArray[5] == list[5]:
        oneWord1.config(bg="green")
        oneWord2.config(bg="green")
        oneWord3.config(bg="green")
        oneWord4.config(bg="green")
        oneWord5.config(bg="green")
        oneWord6.config(bg="green")
        winningPrompt = "CONGRATS!!! The word was: " + electedWord
        prompt.config(text=winningPrompt) 
        
    else:
        oneWord1.config(bg=determineColor(list)[0])
        oneWord2.config(bg=determineColor(list)[1])
        oneWord3.config(bg=determineColor(list)[2])
        oneWord4.config(bg=determineColor(list)[3])
        oneWord5.config(bg=determineColor(list)[4])
        oneWord6.config(bg=determineColor(list)[5]) 
        
def checkAnswerTwo(list):
    
    #Case 1: the answer is correct
    if electedArray[0] == list[0] and electedArray[1] == list[1] and electedArray[2] == list[2] and electedArray[3] == list[3] and electedArray[4] == list[4] and electedArray[5] == list[5]:
        twoWord1.config(bg="green")
        twoWord2.config(bg="green")
        twoWord3.config(bg="green")
        twoWord4.config(bg="green")
        twoWord5.config(bg="green")
        twoWord6.config(bg="green")
        winningPrompt = "CONGRATS!!! The word was: " + electedWord
        prompt.config(text=winningPrompt) 
        
    else:
        twoWord1.config(bg=determineColor(list)[0])
        twoWord2.config(bg=determineColor(list)[1])
        twoWord3.config(bg=determineColor(list)[2])
        twoWord4.config(bg=determineColor(list)[3])
        twoWord5.config(bg=determineColor(list)[4])
        twoWord6.config(bg=determineColor(list)[5]) 

def checkAnswerThree(list):
    
    #Case 1: the answer is correct
    if electedArray[0] == list[0] and electedArray[1] == list[1] and electedArray[2] == list[2] and electedArray[3] == list[3] and electedArray[4] == list[4] and electedArray[5] == list[5]:
        threeWord1.config(bg="green")
        threeWord2.config(bg="green")
        threeWord3.config(bg="green")
        threeWord4.config(bg="green")
        threeWord5.config(bg="green")
        threeWord6.config(bg="green")
        winningPrompt = "CONGRATS!!! The word was: " + electedWord
        prompt.config(text=winningPrompt) 
        
    else:
        threeWord1.config(bg=determineColor(list)[0])
        threeWord2.config(bg=determineColor(list)[1])
        threeWord3.config(bg=determineColor(list)[2])
        threeWord4.config(bg=determineColor(list)[3])
        threeWord5.config(bg=determineColor(list)[4])
        threeWord6.config(bg=determineColor(list)[5]) 

def checkAnswerFour(list):
    
    #Case 1: the answer is correct
    if electedArray[0] == list[0] and electedArray[1] == list[1] and electedArray[2] == list[2] and electedArray[3] == list[3] and electedArray[4] == list[4] and electedArray[5] == list[5]:
        fourWord1.config(bg="green")
        fourWord2.config(bg="green")
        fourWord3.config(bg="green")
        fourWord4.config(bg="green")
        fourWord5.config(bg="green")
        fourWord6.config(bg="green")
        winningPrompt = "CONGRATS!!! The word was: " + electedWord
        prompt.config(text=winningPrompt) 
        
    else:
        fourWord1.config(bg=determineColor(list)[0])
        fourWord2.config(bg=determineColor(list)[1])
        fourWord3.config(bg=determineColor(list)[2])
        fourWord4.config(bg=determineColor(list)[3])
        fourWord5.config(bg=determineColor(list)[4])
        fourWord6.config(bg=determineColor(list)[5])

def checkAnswerFive(list):
    
    #Case 1: the answer is correct
    if electedArray[0] == list[0] and electedArray[1] == list[1] and electedArray[2] == list[2] and electedArray[3] == list[3] and electedArray[4] == list[4] and electedArray[5] == list[5]:
        fiveWord1.config(bg="green")
        fiveWord2.config(bg="green")
        fiveWord3.config(bg="green")
        fiveWord4.config(bg="green")
        fiveWord5.config(bg="green")
        fiveWord6.config(bg="green")
        winningPrompt = "CONGRATS!!! The word was: " + electedWord
        prompt.config(text=winningPrompt) 
        
    else:
        fiveWord1.config(bg=determineColor(list)[0])
        fiveWord2.config(bg=determineColor(list)[1])
        fiveWord3.config(bg=determineColor(list)[2])
        fiveWord4.config(bg=determineColor(list)[3])
        fiveWord5.config(bg=determineColor(list)[4])
        fiveWord6.config(bg=determineColor(list)[5])
        
        
        
        
        
#makes sure the tracing is working   
def callback(sv):
    print (sv.get())
        
    


















#Setting up the Title (TheThedle) and prompt box
title1 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="T",font="Helvetica")
title1.place(x=27,y=40)
title2 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="H",font="Helvetica")
title2.place(x=87,y=40)
title3 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="E",font="Helvetica")
title3.place(x=147,y=40)

title4 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="T",font="Helvetica")
title4.place(x=207,y=40)
title5 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="H",font="Helvetica")
title5.place(x=267,y=40)
title6 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="E",font="Helvetica")
title6.place(x=327,y=40)

title7 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="D",font="Helvetica")
title7.place(x=387,y=40)
title8 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="L",font="Helvetica")
title8.place(x=447,y=40)
title9 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="E",font="Helvetica")
title9.place(x=507,y=40)
title10 = tk.Label(background,bg="#dbbaf2",width=4,height=2,text="!",font="Helvetica")
title10.place(x=567,y=40)

prompt = tk.Label(background,bg="#dbbaf2",width=40,height=4,text="Hello User, Welcome to TheThedle!\nType your answer into the pink box and press *enter*\nGood Luck!!!",font=("Helvetica",14))
prompt.place(x=98,y=525)



#Setting up the boxes for the first word
oneWord1 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
oneWord1.place(x=95,y=150)
oneWord2 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
oneWord2.place(x=175,y=150)
oneWord3 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
oneWord3.place(x=255,y=150)
oneWord4 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
oneWord4.place(x=335,y=150)
oneWord5 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
oneWord5.place(x=415,y=150)
oneWord6 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
oneWord6.place(x=495,y=150)

#Getting the user's selection and checking the status of the word compared to the original word
sv1 = StringVar()
sv1.trace("w", lambda name, index, mode, sv1=sv1: callback(sv1))
oneWord = tk.Entry(bg="#dbbaf2",font=("Helvetica",1),textvariable=sv1,)
oneWord.bind('<Return>',setWordOne)
oneWord.place(x=100,y=250)




#Setting up the boxes for the second word
twoWord1 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
twoWord1.place(x=95,y=220)
twoWord2 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
twoWord2.place(x=175,y=220)
twoWord3 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
twoWord3.place(x=255,y=220)
twoWord4 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
twoWord4.place(x=335,y=220)
twoWord5 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
twoWord5.place(x=415,y=220)
twoWord6 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
twoWord6.place(x=495,y=220)

#Getting the user's selection and checking the status of the word compared to the original word
sv2 = StringVar()
sv2.trace("w", lambda name, index, mode, sv2=sv2: callback(sv2))
twoWord = tk.Entry(bg="#dbbaf2",font=("Helvetica",1),textvariable=sv2,)
twoWord.bind('<Return>',setWordTwo)




#Setting up the boxes for the third word
threeWord1 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
threeWord1.place(x=95,y=290)
threeWord2 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
threeWord2.place(x=175,y=290)
threeWord3 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
threeWord3.place(x=255,y=290)
threeWord4 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
threeWord4.place(x=335,y=290)
threeWord5 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
threeWord5.place(x=415,y=290)
threeWord6 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
threeWord6.place(x=495,y=290)

sv3 = StringVar()
sv3.trace("w", lambda name, index, mode, sv3=sv3: callback(sv3))
threeWord = tk.Entry(bg="#dbbaf2",font=("Helvetica",1),textvariable=sv3,)
threeWord.bind('<Return>',setWordThree)








#Setting up the boxes for the fourth word
fourWord1 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fourWord1.place(x=95,y=360)
fourWord2 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fourWord2.place(x=175,y=360)
fourWord3 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fourWord3.place(x=255,y=360)
fourWord4 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fourWord4.place(x=335,y=360)
fourWord5 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fourWord5.place(x=415,y=360)
fourWord6 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fourWord6.place(x=495,y=360)

sv4 = StringVar()
sv4.trace("w", lambda name, index, mode, sv4=sv4: callback(sv4))
fourWord = tk.Entry(bg="#dbbaf2",font=("Helvetica",1),textvariable=sv4,)
fourWord.bind('<Return>',setWordFour)



#Setting up the boxes for the fifth word
fiveWord1 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fiveWord1.place(x=95,y=430)
fiveWord2 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fiveWord2.place(x=175,y=430)
fiveWord3 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fiveWord3.place(x=255,y=430)
fiveWord4 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fiveWord4.place(x=335,y=430)
fiveWord5 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fiveWord5.place(x=415,y=430)
fiveWord6 = tk.Label(background,bg="gray",width=4,height=2,font="Helvetica",text="")
fiveWord6.place(x=495,y=430)

sv5 = StringVar()
sv5.trace("w", lambda name, index, mode, sv5=sv5: callback(sv5))
fiveWord = tk.Entry(bg="#dbbaf2",font=("Helvetica",1),textvariable=sv5,)
fiveWord.bind('<Return>',setWordFive)















root.mainloop()