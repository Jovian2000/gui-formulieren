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