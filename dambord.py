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