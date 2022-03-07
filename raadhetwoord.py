import tkinter as tk
from tkinter.messagebox import *
from tkinter import *
import string
import random

root = tk.Tk()
root.geometry("1000x500")
root.title("Raad het woord - speler 1")

textInfo = ""
alphabetList = list(string. ascii_lowercase)
boxList = []
win = False
correctLetters = 0
guessword = tk.StringVar()
points = 0

def setWord():
    frameGame = tk.Frame(root)
    frameGame.pack(expand = True)
    labelGame = tk.Label(
        frameGame, 
        text = "Vul een woord in",
        font = ("arial", 16)
        )       
    labelGame.grid(row = 0, column = 1)

    def wordSet():
        global textInfo, points
        answer = guessword.get()
        answerList = []
        answerList.extend(answer)
        points = len(answerList) * len(answerList)

        def againOrNot():
            global win
            answerText = guessword.get()
            if win == True:
                gameMessage = "U heeft het woord geraden.\nUw score: " + str(points) + "\nWilt u nog een keer spelen?"
            else:
                gameMessage = "Game over het woord was " + answerText + "\nWilt u nog een keer spelen?"
            question = askyesno(
                title = "Game over!",
                message = gameMessage)
            if question:
                frameGame.destroy()
                root.title("Raad het woord - speler 1")
                win = False
                setWord()
            else:
                root.destroy()

        if len(answerList) >= 4 and len(answerList) <= 7:
            root.title("Raad het woord - speler 2")
            labelGame.destroy()

            labelGame2 = tk.Label(
                frameGame,
                text = "Raad het woord",
                font = ("arial", 16)
                )
            labelGame2.grid(row = 0, columnspan = len(answerList))

            guesswordEntry.destroy()
            labelText.destroy()
            buttonGame.destroy()
            
            currentLetters = []
            for i in range(len(answerList)):
                currentLetters.append(StringVar())
                random.shuffle(alphabetList)
                alphabetList.remove(answerList[i])
                boxList.extend(alphabetList[0:4])
                boxList.append(answerList[i])
                random.shuffle(boxList)
                letterBox = tk.Spinbox (
                    frameGame,
                    values = boxList,
                    textvariable = currentLetters[i],
                    justify ="center",
                    wrap = True,
                    state ="readonly",
                    width = 4
                )
                letterBox.grid(row = 1, column = i)
                alphabetList.extend(answerList[i])
                boxList.clear()
            
            def guessing():
                global points, win, correctLetters
                userGuess = ""
                for x in currentLetters:                    
                    userGuess += str(x.get())
                userGuessList = list(userGuess)
                if userGuess == answer:
                    win = True    
                    againOrNot()
                else:
                    correctLetters = 0
                    for i in range(len(userGuessList)):
                        if userGuessList[i] != answerList[i]:
                            points -= 2
                        else:
                            correctLetters += 1
                    wrongWord()
                if points <= 0:
                    againOrNot()

            buttonGame2 = tk.Button(
            frameGame,
            text = "Doe een gok",
            command = guessing
            )
            buttonGame2.grid(row = 3, columnspan = len(answerList)) 
            print(points)

        else:
            if len(answerList) < 4:
                textInfo = "U heeft te weinig letters in uw woord"
            else:
                textInfo = "U heeft te veel letters in uw woord"
            wrong()

    guesswordEntry = tk.Entry(frameGame, textvariable = guessword)
    guesswordEntry.grid(row = 1, column = 1)

    labelText = tk.Label(
        frameGame,
        text = "(4 tot 7 letters)"    
    )
    labelText.grid(row = 2, column =1)

    buttonGame = tk.Button(
        frameGame,
        text = "Stel woord in",
        command = wordSet)
    buttonGame.grid(row = 3, column = 1)

    def wrongWord():
        if correctLetters == 1:
            pointsText = "Helaas, er is " + str(correctLetters) + " letter goed"
        else:
            pointsText = "Helaas, er zijn " + str(correctLetters) + " letters goed"
        wrongInfo = showerror(
            title = "Fout!",
            message = pointsText
        )

def wrong():
    info = showerror(
        title = "Oeps!!",
        message = textInfo
    )

setWord()

root.mainloop()