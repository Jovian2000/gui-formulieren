import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Dambord")

blackFrame = tk.Label(root, bg = "black")
blackFrame.grid(column = 0, row = 0,  ipadx = 10, ipady = 10)

root.mainloop()