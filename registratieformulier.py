import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import calendar

root = tk.Tk()
root.geometry("800x800")
root.title("Registration Form")

userCode = 10000000

def functionForm():
    global userCode

    def checkForm():
        dictForm = {}
        emptyList = []

        nameCheck = strVarName.get()
        emailCheck = strVarEmail.get()
        addressCheck = strVarAddress.get()
        codeCheck = strVarCode.get()
        telNumberCheck = intVarTelNumber.get()
        genderCheck = selectedGender.get()
        birthDayCheck = intVarDay.get()
        birthMonthCheck = strVarMonth.get()
        birthYearCheck = intVarYear.get()
        dateIncidentCheck = strVarDateIncident.get()
        timeIncidentCheck = strVarTimeIncident.get()
        placeIncidentCheck = strVarPlaceIncident.get()
        incidentCheck = selectedIncident.get()
        caseCheck = selectedCase.get()
        gender2Check = selectedGender2.get()
        lenghtCheck = intVarLength.get()
        postureCheck = selectedPosture.get()
        characteristicsCheck = strVarCharacteristics.get()

        for i,k in dictForm.items():
            if k == "":
                emptyList.append(i)
        # "\n.join"(emptyList) zorgt ervoor dat bij de pop-up alles wat er in de lijst staat, onder elkaar word gezet
        if len(emptyList) > 0:
            showerror(
                title = "Oeps",
                message = "Je hebt het volgende nog niet ingevuld:\n" + "\n".join(emptyList)
            )
        else:
            dictForm.update({"Naam:" : nameCheck})
            dictForm.update({"E-mail:" : emailCheck})
            dictForm.update({"Adres:" : addressCheck })
            dictForm.update({"Postcode:" : codeCheck})
            dictForm.update({"Telefoonnummer:" : telNumberCheck})
            dictForm.update({"Geslacht:" : genderCheck})
            dictForm.update({"Geboortedatum:" : (str(birthDayCheck) + "-" + str(birthMonthCheck) + "-" + str(birthYearCheck))})
            dictForm.update({"Datum incident:" : dateIncidentCheck})
            dictForm.update({"Tijd incident:" : timeIncidentCheck})
            dictForm.update({"Plaats incident:" : placeIncidentCheck})
            dictForm.update({"Wat is er gebeurd:" : incidentCheck})
            dictForm.update({"Wat was de aanleiding:" : caseCheck})
            dictForm.update({"Geslacht (dader):" : gender2Check})
            dictForm.update({"Lengte (in centimeter):" : lenghtCheck})
            dictForm.update({"Postuur:" : postureCheck})
            dictForm.update({"Andere kenmerken:" : characteristicsCheck})
            showinfo(
                title = "Gelukt",
                message = "U heeft alles ingevuld"
            )
            frameForm.destroy()
            frameForm2.destroy()
            frameForm3.destroy()
            frameForm4.destroy()
            frameForm5.destroy()
            frameForm6.destroy()
            frameForm7.destroy()
            checkFormButton.destroy()
            
            dictFormKeys = tk.Label(
                root,
                text = "\n".join(dictForm.keys()),
                font = ("Arial", 12),
                justify = "left"
            )
            dictFormKeys.place(x = 200, y = 200)

            dictFormValues = tk.Label(
                root,
                text = dictFormMatter(dictForm),
                font = ("Arial", 12),
                justify = "left"
            )
            dictFormValues.place(x = 380, y = 200)

            userCodeLabel = tk.Label(
                root,
                text = "registratienummer: " + str(userCode),
                font = ("Arial", 12)
            )
            userCodeLabel.place(x = 300, y = 600)
            
            def restart():
                answer = askyesno(
                    title = "Versturen",
                    message = "Weet u zeker dat u dit wilt versturen?"
                )
                if answer:
                    dictFormKeys.destroy()
                    dictFormValues.destroy()
                    userCodeLabel.destroy()
                    restartButton.destroy()
                    functionForm()

            restartButton = tk.Button(
                root,
                text = "Nieuwe formulier",
                command = restart,
                font = ("Arial", 12)
            )
            restartButton.place(x = 300, y = 650)

    def dictFormMatter(dictToFormat) -> str:
        returnString = ""
        for k, v in dictToFormat.items():
            returnString += (str(v) + "\n")
        return returnString
        
    # Eerste frame
    frameForm = tk.Frame(root)
    frameForm.place(x = 230, y = 70)

    titleLabel = tk.Label(
        frameForm,
        text = "Meldingsformulier incident",
        font = ("Arial", 16, "bold")
    )
    titleLabel.grid(row = 0, columnspan = 2)

    labelName = tk.Label(
        frameForm,
        text = "Naam:",
        font = ("Arial", 12)
    )
    labelName.grid(row = 1, column = 0, sticky = "w")

    strVarName = tk.StringVar()
    entryName = tk.Entry(
        frameForm,
        textvariable = strVarName,
        font = ("Arial", 12),
        width = 25
    )
    entryName.grid(row = 1, column = 1)

    labelEmail = tk.Label(
        frameForm,
        text = "E-mail:",
        font = ("Arial", 12)
    )
    labelEmail.grid(row = 2, column = 0, sticky = "w")

    strVarEmail = tk.StringVar()
    entryEmail = tk.Entry(
        frameForm,
        textvariable = strVarEmail,
        font = ("Arial", 12),
        width = 25
    )
    entryEmail.grid(row = 2, column= 1)

    labelAddress = tk.Label(
        frameForm,
        text = "Adres:",
        font = ("Arial", 12)
        )
    labelAddress.grid(row = 3, column = 0, sticky = "w")

    strVarAddress = tk.StringVar()
    entryAddress = tk.Entry(
        frameForm,
        textvariable = strVarAddress,
        font = ("Arial", 12),
        width = 25
    )
    entryAddress.grid(row =3 , column = 1)

    labelCode = tk.Label(
    frameForm,
    text = "Postcode:",
    font = ("Arial", 12)
    )
    labelCode.grid(row = 4, column = 0, sticky = "w")

    strVarCode = tk.StringVar()
    entryCode = tk.Entry(
        frameForm,
        textvariable = strVarCode,
        font = ("Arial", 12),
        width = 25
    )
    entryCode.grid(row = 4 , column = 1)

    labelTelNumber = tk.Label(
        frameForm,
        text = "Telefoonnummer:",
        font = ("Arial", 12)
    )
    labelTelNumber.grid(row = 5 , column = 0, sticky = "w")

    intVarTelNumber = tk.IntVar()
    entryTelNumber = tk.Entry(
        frameForm,
        textvariable = intVarTelNumber,
        font = ("Arial", 12),
        width = 25
    )    
    entryTelNumber.grid(row = 5 , column = 1)

    # Tweede frame
    frameForm2 = tk.Frame(root)
    frameForm2.place(x = 210, y = 225)

    labelgender = tk.Label(
        frameForm2,
        text = "Geslacht:",
        font = ("Arial", 12)
    )
    labelgender.grid(row = 0, column = 0, sticky = "w")

    selectedGender = tk.StringVar()
    genders = (("Man", "Man"), ("Vrouw", "Vrouw"), ("Anders", "Anders"))
    n = 1
    for g in genders:
        genderButton = ttk.Radiobutton(
            frameForm2,
            text = g[0],
            value = g[1],
            variable = selectedGender,
        )
        genderButton.grid(row = 0, column = n)
        n +=1

    labelBirth = tk.Label(
        frameForm2,
        text = "Geboortedatum:",
        font = ("Arial", 12)
    )
    labelBirth.grid(row = 1, column = 0, sticky = "w")

    # dit zijn de code voor de datum die ik dus heb gepakt van daysbydateCalc.py
    intVarDay = tk.IntVar()
    dayCombobox = ttk.Combobox(
        frameForm2, 
        textvariable = intVarDay, 
        font = ("Arial", 12),
        justify ="center",
        width = 3
    )
    dayCombobox["values"] = []
    dayCombobox["state"] = "readonly"
    dayCombobox.grid(row = 1, column = 1, sticky = "ew")

    strVarMonth = tk.StringVar(value = "January")
    monthCombobox = ttk.Combobox(
        frameForm2, 
        textvariable = strVarMonth, 
        font = ("Arial", 12),
        justify ="center",
        width = 10
    )
    monthCombobox["values"] = [calendar.month_name[j] for j in range (1,13)]
    monthCombobox["state"] = "readonly"
    monthCombobox.grid(row = 1, column = 2, sticky = "w")

    intVarYear = tk.IntVar(value = 2000)
    yearEntry = ttk.Combobox(
        frameForm2,
        textvariable = intVarYear,
        font = ("Arial", 12),
        justify ="center",
        width = 5
    )
    yearEntry["values"] = [k for k in range (1900,2015)]
    yearEntry["state"] = "readonly"
    yearEntry.grid(row = 1, column = 3, sticky = "w")

    def checkLeapYear():
        chosenYear = intVarYear.get()
        chosenMonth = strVarMonth.get()
        if chosenMonth == "February":
            if (chosenYear % 400 == 0) and (chosenYear % 100 == 0):
                dayCombobox["values"] = [j for j in range(1,30)]
            elif (chosenYear % 4 == 0) and (chosenYear % 100 != 0):
                dayCombobox["values"] = [j for j in range(1,30)]
            else:
                dayCombobox["values"] = [j for j in range(1,29)]

    def daysValue():
        chosenMonth = strVarMonth.get()
        if chosenMonth == "April" or chosenMonth == "June" or chosenMonth == "May" or chosenMonth == "September" or chosenMonth == "November": 
            dayCombobox["values"] = [j for j in range(1,31)]
        else:
            dayCombobox["values"] = [j for j in range(1,32)]
        checkLeapYear()

    def entryCommand(event):
        checkLeapYear() 

    def setDays(event):
        daysValue()

    daysValue()
    yearEntry.bind("<KeyRelease>", entryCommand)
    monthCombobox.bind("<<ComboboxSelected>>", setDays)

    # Derde frame
    frameForm3 = tk.Frame(root)
    frameForm3.place(x = 210, y = 277)

    labelDateIncident = tk.Label(
        frameForm3, 
        text = "Datum incident: ",
        font = ("Arial", 12)
    )
    labelDateIncident.grid(row = 0, column = 0, sticky = "w")

    strVarDateIncident = tk.StringVar()
    entryDateIncident = tk.Entry(
        frameForm3, 
        textvariable = strVarDateIncident,
        font = ("Arial", 12),
        width = 25
    )
    entryDateIncident.grid(row =0, column = 1)

    labelDateInfoIncident = tk.Label(
        frameForm3, 
        text = "(dd-mm-yyyy)",
        font = ("Arial", 10)
    )
    labelDateInfoIncident.grid(row = 0, column = 2)

    labelTimeIncident = tk.Label(
        frameForm3, 
        text = "Tijd incident: ",
        font = ("Arial", 12)
    )
    labelTimeIncident.grid(row = 1, column = 0, sticky = "w")

    strVarTimeIncident = tk.StringVar()
    entryTimeIncident = tk.Entry(
        frameForm3, 
        textvariable = strVarTimeIncident,
        font = ("Arial", 12),
        width = 10
    )
    entryTimeIncident.grid(row =1, column = 1)

    labelTimeInfoIncident = tk.Label(
        frameForm3, 
        text = "(00:00)",
        font = ("Arial", 10)
    )
    labelTimeInfoIncident.grid(row = 1, column = 2)

    labelPlaceIncident = tk.Label(
        frameForm3, 
        text = "Plaats incident: ",
        font = ("Arial", 12)
    )
    labelPlaceIncident.grid(row = 2, column = 0, sticky = "w")

    strVarPlaceIncident = tk.StringVar()
    entryPlaceIncident = tk.Entry(
        frameForm3, 
        textvariable = strVarPlaceIncident,
        font = ("Arial", 12),
        width = 25
    )
    entryPlaceIncident.grid(row =2, column = 1)

    # Vierde frame
    frameForm4 = tk.Frame(root)
    frameForm4.place(x = 80, y = 360)

    labelInfoIncident = tk.Label(
        frameForm4, 
        text = "Wat is er gebeurd: ",
        font = ("Arial", 12)
    )
    labelInfoIncident.grid(row = 0, column = 0)

    selectedIncident = tk.StringVar()
    incidents = (
        ("Schelden", "Schelden"), ("Beledigen", "Beledigen"), ("Vernielen", "Vernielen"), 
        ("Bedreigen", "Bedreigen"), ("Diefstal", "Diefstal"), ("Discrimeneren", "Discrimineren"), 
        ("Sexuele intimidatie", "Sexuele intimidatie"), ("Slaan en/of schoppen", "Slaan/schoppen"), 
        ("Mes/steekwapen", "Mes/steekwapen"), ("Vuurwapen", "Vuurwapen"), ("Overval", "Overval"))
    h = 0
    b = 1
    for i in incidents:
        incidentsButton = ttk.Radiobutton(
            frameForm4,
            text = i[0],
            value = i[1],
            variable = selectedIncident,
        )
        incidentsButton.grid(row = h, column = b, sticky = "ew")
        b +=1
        if b > 3:
            h += 1
            b = 1

    labelCaseIncidents = tk.Label(
        frameForm4,
        text = "Wat was de aanleiding:",
        font = ("Arial", 12)
    )
    labelCaseIncidents.grid(row = 4, column = 0)

    selectedCase = tk.StringVar()
    cases = (
        ("Onbekend", "Onbekend"), ("Betaling", "Betaling"), ("Ontevreden over dienstverlening", "Ontevreden over dienstverlening"),
        ("Dronken", "Dronken"), ("Vuurwapen", "Vuurwapen"), ("Weigering aan regels te houden", "Weigering aan regels te houden"),
    )
    num = 4
    num1 = 1
    for x in cases:
        caseButtons = ttk.Radiobutton(
            frameForm4, 
            text = x[0], 
            value = x[1],
            variable = selectedCase
        )
        caseButtons.grid(row = num, column = num1)
        num1 += 1
        if num1 > 3:
            num += 1
            num1 = 1

    # vijfde frame
    frameForm5 = tk.Frame(root)
    frameForm5.place(x = 210, y = 510)

    labelData = tk.Label(
        frameForm5,
        text = "Gegevens van de dader",
        font = ("Arial", 12, "bold")
    )
    labelData.pack()

    # zesde frame
    frameForm6 = tk.Frame(root)
    frameForm6.place(x= 130, y = 535)

    labelGender2 = tk.Label(
        frameForm6,
        text = "Geslacht:",
        font = ("Arial", 12)
    )
    labelGender2.grid(row = 0, column = 0, sticky = "w")

    selectedGender2 = tk.StringVar()
    n = 1
    for g in genders:
        genderButton = ttk.Radiobutton(
            frameForm6,
            text = g[0],
            value = g[1],
            variable = selectedGender2,
        )
        genderButton.grid(row = 0, column = n,)
        n +=1

    labelLength = tk.Label(
        frameForm6,
        text = "Lengte (in centimeter):",
        font = ("Arial", 12)
    )
    labelLength.grid(row = 1, column = 0, sticky = "w")

    intVarLength = tk.IntVar()
    entryLength = tk.Entry(
        frameForm6,
        textvariable = intVarLength,
        font = ("Arial", 12),
        width = 5
    )
    entryLength.grid(row = 1, column = 1)

    labelPosture = tk.Label(
        frameForm6,
        text = "Postuur:",
        font = ("Arial", 12)
    )
    labelPosture.grid(row = 2, column =0, sticky = "w")

    selectedPosture = tk.StringVar()
    choicesPosture = (("Gezet", "Gezet"), ("Atletisch", "Atletisch"), ("Slank", "Slank"))
    n = 1
    for c in choicesPosture:
        postureButtons = ttk.Radiobutton(
            frameForm6,
            text = c[0],
            value = c[1],
            variable = selectedPosture
        )
        postureButtons.grid(row = 2, column = n)
        n += 1

    # zevende frame
    frameForm7 = tk.Frame(root)
    frameForm7.place(x= 130, y = 605)

    labelCharacteristics = tk.Label(
        frameForm7,
        text = "Andere kenmerken:",
        font = ("Arial", 12)
    )
    labelCharacteristics.grid(row =0, column = 0, sticky = "w")

    strVarCharacteristics = tk.StringVar()
    entryCharacteristics = tk.Entry(
        frameForm7,
        textvariable = strVarCharacteristics,
        font = ("Arial", 12),
        width = 25
    )
    entryCharacteristics.grid(row = 0, column = 1)

    checkFormButton = tk.Button(
        root,
        text = "Inleveren",
        command = checkForm,
        font = ("Arial", 14)
    )
    checkFormButton.place(x = 420, y = 640)

    userCode += 1

functionForm()

root.mainloop()
