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
