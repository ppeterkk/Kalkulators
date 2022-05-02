from ast import operator
from tkinter import*
from math import*

mansLogs = Tk()
mansLogs.title("Kalkulators")
# mansLogs.geometry("300x300") - izmērs

def btnClick(number):
    current = e.get()
    # nolasa esošo skaitli
    e.delete(0, END)
    # nodzēš iepriekšējo skaitli
    newNumber = str(current) + str(number)
    e.insert(0, newNumber)
    # ievieto displejā
    return 0
    # ja nav skaitlis, ko atgriezt, tad raksta return 0

def btnCommand(command):
    global num1
    # jāiegaumē skaitlis un darbība
    global mathOp
    mathOp = command
    num1 = int(e.get())
    e.delete(0, END)
    return 0

def vienads():
    num2 = int(e.get())
    result = 0
    if mathOp == "+":
        result = num1 + num2
    elif mathOp == "-":
        result = num1 - num2
    elif mathOp == "*":
        result = num1 * num2
    elif mathOp == "/":
        result = num1 / num2
    else:
        result = 0
    e.delete(0, END)
    e.insert(0, str(result))
    return 0

def clear():
    e.delete(0, END)
    num1 = 0
    mathOp = ""
    return 0

def kapinasana():
    global operator
    global num1
    global mathOp
    num1 = (int(e.get()))
    num1 = num1**2
    e.delete(0, END)
    e.insert(0, num1)
    return 0

def kvadrSakne():
    global operator
    global num1
    global mathOp
    num1 = (int(e.get()))
    num1 = sqrt(num1)
    e.delete(0, END)
    e.insert(0, num1)
    return 0

def procenti():
    global operator
    global num1
    global mathOp
    num1 = (float(e.get()))
    num1 = "{:.0%}". format(num1)
    e.delete(0, END)
    e.insert(0, num1)
    return 0

def logaritms():
    global operator
    global num1
    global mathOp
    num1 = (int(e.get()))
    num2 = log10(num1)
    # bāze - 10
    e.delete(0, END)
    e.insert(0, num2)
    return 0

# izveido pogas
e = Entry(mansLogs, width = 15, bd = 20, bg = "#F5F5F5", font = ("Trebuchet MS", 20))
# displeja logs, kurā ievada skaitļus

btn0 = Button(mansLogs, text="0", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(0))
btn1 = Button(mansLogs, text="1", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(1))
btn2 = Button(mansLogs, text="2", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(2))
btn3 = Button(mansLogs, text="3", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(3))
btn4 = Button(mansLogs, text="4", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(4))
btn5 = Button(mansLogs, text="5", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(5))
btn6 = Button(mansLogs, text="6", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(6))
btn7 = Button(mansLogs, text="7", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(7))
btn8 = Button(mansLogs, text="8", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(8))
btn9 = Button(mansLogs, text="9", padx="30", pady="20", bd = 5, bg = "#A9A9A9", command = lambda:btnClick(9))

btnSask = Button(mansLogs, text="+", padx="28", pady="20", bd = 5, command = lambda:btnCommand("+"))
btnAtn = Button(mansLogs, text="-", padx="30", pady="20", bd = 5, command = lambda:btnCommand("-"))
btnReiz = Button(mansLogs, text="*", padx="30", pady="20", bd = 5, command = lambda:btnCommand("*"))
btnDal = Button(mansLogs, text="/", padx="30", pady="20", bd = 5, command = lambda:btnCommand("/"))

btnKvadr = Button(mansLogs, text="√", padx="30", pady="20", bd = 5, command = kvadrSakne)
btnKapin = Button(mansLogs, text="x²", padx="30", pady="20", bd = 5, command = kapinasana)
btnProc = Button(mansLogs, text="%", padx="27.5", pady="20", bd = 5, command = procenti)
btnLogar = Button(mansLogs, text="log", padx="25", pady="20", bd = 5, command = logaritms)

btnVien = Button(mansLogs, text="=", padx="30", pady="20", bd = 5, command = vienads)
btnDel = Button(mansLogs, text="C", padx="30", pady="20", bd = 5, bg = "#FF4500", command = clear)

# definē pogu novietojumu
e.grid(row=0, column=0, columnspan=4)

btn0.grid(row=5, column=1)
btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

btnSask.grid(row=5, column=3)
btnAtn.grid(row=4, column=3)
btnReiz.grid(row=3, column=3)
btnDal.grid(row=2, column=3)

btnKvadr.grid(row=1, column=2)
btnKapin.grid(row=5, column=0)
btnProc.grid(row=1, column=3)
btnLogar.grid(row=1, column=1)

btnVien.grid(row=5, column=2)
btnDel.grid(row=1, column=0)

mansLogs.mainloop()