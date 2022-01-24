import tkinter as tk

root = tk.Tk()
root.title("Clicker")
root.geometry("200x200")
root.configure(bg = "grey")
count = 0
countCheck = ""
BoxState = "disabled"

def autoClick():
    global countCheck
    checkBox = autoClickBoxVar.get()
    if checkBox == 1:
        if countCheck == "Up":
            up()
        elif countCheck == "Down":
            down()
        root.after(100,autoClick)

def multiplyOrDivide(event):
    global count, countCheck
    if countCheck == "Up":
        count *= 3
    elif countCheck == "Down":
        count /= 3 
    countLabel.configure(text = count)

def yellowBackground(event):
    root.configure(bg = "yellow")

def colourChanges(event):
    global count
    if count > 0:
        root.configure(bg = "green")
    elif count < 0:
        root.configure(bg = "red")
    else:
        root.configure(bg = "grey")

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

def upButton(event):
    up()

def downButton(event):
    down()

def spaceButton(event):
    multiplyOrDivide("")

buttonUp = tk.Button(
    root,
    command = up,
    text = "Up"    
)
buttonUp.pack(
    ipadx = 55,  
    side = "top",
    expand = True
)

countLabel = tk.Label(
    root,
    text = count    
)
countLabel.pack(
    ipadx = 60,
    expand = True
)

buttonDown = tk.Button(
    root,
    command = down,
    text = "Down"
)
buttonDown.pack(
    ipadx = 45, 
    side = "bottom",
    expand = True
)

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

countLabel.bind("<Enter>", yellowBackground)
countLabel.bind("<Leave>", colourChanges)
countLabel.bind("<Double-Button>", multiplyOrDivide)
root.bind("<Up>", upButton) and root.bind("<+>", upButton)
root.bind("<Down>", downButton) and root.bind("-", downButton)
root.bind("<space>", spaceButton)
root.mainloop()