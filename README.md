# gui-formulieren
## F1.8.03.L1 - Simple FPS trainer v2
Ik heb de entry erbij geplaatst
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