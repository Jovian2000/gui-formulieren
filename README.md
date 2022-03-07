# gui-formulieren
## F1.8.03.L1 - Simple FPS trainer v2
Ik heb de entry erbij geplaatst, je kan nu kiezen hoeveel seconde je wilt
``` python
timePickLabel = tk.Label(
    root, 
    text = "Choose time (in seconds)", 
    font =("Arial", 13),
    bg = "DarkOliveGreen4",
    fg = "black")
timePickLabel.pack()
timePickLabel.place(relx = 0.5, rely = 0.2, anchor = "center")

timePickEntry = tk.Entry(root, textvariable = timeValue, font = ("Arial", 13), justify ="center")
timePickEntry.pack()
timePickEntry.place(relx = 0.5, rely = 0.25, anchor = "center")

root.mainloop()
```
En ik heb nu int- en stringVariables gebruikt
``` python
root = tk.Tk()
root.title("Simple FPS trainer")
root.geometry("500x500")
root.configure(bg="DarkOliveGreen4")
timeValue = tk.IntVar(value=20)
textTime = tk.StringVar(value ="Time remaining: ")
points = 0
taskLists = ["w", "a", "s", "d", "space", "<Button>", "<Double-Button>", "<Triple-Button>"]
remainingTimeText = textTime.get()
```
``` python 
def start():
    startButton.destroy()
    timePickEntry.destroy()
    timePickLabel.destroy()
    timer = timeValue.get()
    timeValue.set(timer-1)
    textTime.set(remainingTimeText + str(timer))
    labelTimer.configure(textvariable=textTime)
    if timer > 0:
        root.after(1000, start)
    else:
        YesOrNo()
```
### Aanpassingen 
Ik heb wat nutteloze packs weggehaald
## F1.8.03.L2 - Autoclicker (Clicker v5)
Ik heb de clickerV4 aangepast. Er is nu een checkbox voor autoclicker.
``` python
def autoClick():
    global countCheck
    checkBox = autoClickBoxVar.get()
    if checkBox == 1:
        if countCheck == "Up":
            up()
        elif countCheck == "Down":
            down()
        root.after(500,autoClick)
```
``` python
def up():
    global count, countCheck
    count += 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Up"
    autoClickBox.configure(state = "normal")
def down():
    global count, countCheck
    count -= 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Down"
    autoClickBox.configure(state = "normal")
```
``` python
autoClickBoxVar = tk.IntVar()
autoClickBox = tk.Checkbutton(
    root, 
    text = "Autoclick",
    command = autoClick,
    variable = autoClickBoxVar,
    state = "disabled",
    onvalue = 1, 
    offvalue = 0
    )
autoClickBox.pack()
```
## F1.8.03.L4 - een Dambord
Dambord gemaakt
``` python
import tkinter as tk

root = tk.Tk()
root.geometry("800x800")
root.title("Dambord")

frame = tk.Frame(root)

v = False
for j in range(10):
    if v == True:
        v = False
    else:
        v = True
    for o in range(10):
        if v == True:
            colour = "black"
            v = False
        else: 
            colour = "white"
            v = True
        tile = tk.Label(frame, bg = colour, padx = 30, pady = 20)
        tile.grid(row = j, column = o)
frame.pack(expand = True)

root.mainloop()
```
## F1.8.03.O2 - Days by date calculator
Hierbij de dagen calculator
``` python
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import datetime as dt
import calendar

root = tk.Tk()
root.geometry("800x500")
root.title("Days by date calculator")
root.config(bg = "black")

def calculate():
    global number, textInfo
    dayPicked = selectedDay.get() 
    monthPicked = selectedMonth.get()
    yearPicked = selectedYear.get()
    monthNumber = dt.datetime.strptime(monthPicked, "%B").month
    today = date
    datePicked = dt.date(yearPicked, monthNumber, dayPicked)
    difference = datePicked - today
    number = difference.days
    if number > 0:
        if number == 1:
            textInfo = "This is " + str(number) + " day in the future"
        else:
            textInfo = "This is " + str(number) + " days in the future"
    elif number < 0:
        if -number == 1:
            textInfo = "This was " + str(-number) + " day ago"
        else:
            textInfo = "This was " + str(-number) + " days ago"
    else:
        textInfo = "This is today"

def checkLeapYear():
    chosenYear = selectedYear.get()
    chosenMonth = selectedMonth.get()
    if chosenMonth == "February":
        if (chosenYear % 400 == 0) and (chosenYear % 100 == 0):
            dayCombobox["values"] = [j for j in range(1,30)]
        elif (chosenYear % 4 == 0) and (chosenYear % 100 != 0):
            dayCombobox["values"] = [j for j in range(1,30)]
        else:
            dayCombobox["values"] = [j for j in range(1,29)]

def entryCommand(event):
    checkLeapYear()

def daysValue():
    chosenMonth = selectedMonth.get()
    if chosenMonth == "April" or chosenMonth == "June" or chosenMonth == "May" or chosenMonth == "September" or chosenMonth == "November": 
        dayCombobox["values"] = [j for j in range(1,31)]
    else:
        dayCombobox["values"] = [j for j in range(1,32)]
    checkLeapYear()

def setDays(event):
    daysValue()

frame = tk.Frame(root, bg = "grey4")

labelDate = tk.Label(
    frame, 
    text = "Date:",
    font = ("Arial", 16),
    bg = "grey8",
    fg = "snow"
)
labelDate.grid(row = 1, column = 2)

date = dt.date.today()
currentDay = f"{date:%d}"
currentMonth = f"{date:%B}"
currentYear = f"{date:%Y}"

selectedDay = tk.IntVar(value = currentDay)
selectedMonth = tk.StringVar(value = currentMonth)
selectedYear = tk.IntVar(value = currentYear)

dayCombobox = ttk.Combobox(
    frame, 
    textvariable = selectedDay, 
    font = ("Arial", 14),
    justify ="center"
)
dayCombobox["values"] = []
dayCombobox["state"] = "readonly"
dayCombobox.grid(row = 3, column = 1)

monthCombobox = ttk.Combobox(
    frame, 
    textvariable = selectedMonth, 
    font = ("Arial", 14),
    justify ="center"
)
monthCombobox["values"] = [calendar.month_name[j] for j in range (1,13)]
monthCombobox["state"] = "readonly"
monthCombobox.grid(row = 3, column = 2)

yearEntry = ttk.Entry(
    frame, 
    textvariable = selectedYear,
    font = ("Arial",14),
    justify ="center"
)
yearEntry.grid(row = 3, column = 3)

button = tk.Button(
    frame,
    command = lambda:[calculate(), showinfo(
        title = "Date",
        message = textInfo
    )],
    text = "Go",
    font = ("Arial", 14),
    padx = 20,
    pady = 1,
    bg = "grey8",
    fg = "snow"
)
button.grid(row = 4, column = 2)

frame.pack(expand = True)

labelInfo = tk.Label(
    root,
    text = "Note: Press Enter when you have entered the year",
    font = ("Arial", 9),
    bg = "black",
    fg = "snow"
)
labelInfo.place(relx = 0.5, rely = 0.7, anchor = "center")

daysValue()

yearEntry.bind("<Return>", entryCommand)
monthCombobox.bind("<<ComboboxSelected>>", setDays)

root.mainloop()
```
## F1.8.03.O3 - Raad het woord
Hierbij raad het woord
``` python 
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
pointsPerLetter = 0
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
                win = False
                setWord()
            else:
                root.destroy()

        if len(answerList) >= 4 and len(answerList) <= 7:
            root.title("Raad het woord - speler 2")
            labelGame.configure(text = "Raad het woord")
            guesswordEntry.destroy()
            labelText.destroy()
            buttonGame.configure(text = "Doe een gok")
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
                    wrap = True 
                )
                letterBox.grid(row = 1, column = i)
                alphabetList.extend(answerList[i])
                boxList.clear()
            
            def guessing():
                global points, win, pointsPerLetter
                userGuess = ""
                for x in currentLetters:                    
                    userGuess += str(x.get())
                userGuessList = list(userGuess)
                if userGuess == answer:
                    win = True    
                    againOrNot()
                else:
                    pointsPerLetter = 0
                    for i in range(len(userGuessList)):
                        if userGuessList[i] != answerList[i]:
                            points -= 2
                        else:
                            pointsPerLetter += 1
                    wrongWord()
                if points <= 0:
                    againOrNot()

            buttonGame.configure(command = guessing)
            print(answer)
            print(answerList)
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
        if pointsPerLetter == 1:
            pointsText = "Helaas, er is " + str(pointsPerLetter) + " letter goed"
        else:
            pointsText = "Helaas, er zijn " + str(pointsPerLetter) + " letters goed"
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
```
### aanpassingen
Ik heb nog wat aanpassingen gedaan in raadhetwoord.py, i.p.v. dat hij nu de labels en knoppen veranderd, maakt de programma een nieuwe aan.

## F1.8.03.O4 - Een registratie formulier
De laatste opdracht afgemaakt 