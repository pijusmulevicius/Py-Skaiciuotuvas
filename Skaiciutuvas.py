from tkinter import *

root = Tk() # cia main window kuris yra reikalingas
root.title("Skaiciuotuvas")

e = Entry(root, width=32, borderwidth=5) # entry tai tiesiog yra input widgets
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

Ac = "l"
num0=0.0
num1=0.0

#e.insert(0, "default text") #sample textas inputui
def setNum(number):
    current = e.get() #paima stringa esancio number consoleje
    e.delete(0, END)  #istrina sena stringa consoleje, 0 reiskia kad pradetu deletinti nuo string[0], END iki kur, siuo atveju iki galo
    e.insert(0, str(current) + str(number))  #insertina seno stringo kopija su pridetu nauju skaitmeniu

def clear():
    global Ac
    global num0
    global num1
    Ac = ""
    num0 = 0
    num1 = 0
    e.delete(0, END)


def setAction(action):
    global num0
    num0 = float(e.get()) #type castina
    print(num0)
    print(type(num0))
    e.delete(0, END)
    global Ac
    Ac = action


def calculateRez():
    global num0
    global num1
    num1 = float(e.get())
    e.delete(0, END)
    if Ac == "/":
        e.insert(0, num0 / num1)
    elif Ac == "X":
        e.insert(0, num0 * num1)
    elif Ac == "-":
        e.insert(0, num0 - num1)
    elif Ac == "+":
        e.insert(0, num0 + num1)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda : setNum(1)) #lambda yra reikalinga jei nori passinti argumentus i def funkcija
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda : setNum(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda : setNum(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda : setNum(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda : setNum(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda : setNum(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda : setNum(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda : setNum(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda : setNum(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda : setNum(0))


button_dot = Button(root, text=".", padx=40, pady=20, command=lambda : setNum("."))

button_div = Button(root, text="/", padx=40, pady=20, command=lambda : setAction("/"))
button_mul = Button(root, text="X", padx=40, pady=20, command=lambda : setAction("X"))
button_sub = Button(root, text="-", padx=40, pady=20, command=lambda : setAction("-"))
button_add = Button(root, text="+", padx=40, pady=20, command=lambda : setAction("+"))

button_eq = Button(root, text="=", padx=40, pady=20, command=calculateRez)

button_clr = Button(root, text="clear", padx=25, pady=20, command=clear)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)

button_div.grid(row=1,column=3)
button_mul.grid(row=2,column=3)
button_sub.grid(row=3,column=3)
button_add.grid(row=4,column=3)
button_eq.grid(row=4,column=2)
button_clr.grid(row=0,column=3)

#myButton.pack()

root.mainloop()
