import tkinter as tk

root = tk.Tk()
root.geometry("800x800")
root.title("Dambord")

frame = tk.Frame(root)
v = True

for j in range(10):
    v = not v
    for a in range(10):
        if v == False:
            colour = "black"
        else: 
            colour = "white"
        v = not v
        tile = tk.Label(frame, bg = colour, padx = 30, pady = 20)
        tile.grid(row = j, column = a)
frame.pack(expand = True)

root.mainloop()