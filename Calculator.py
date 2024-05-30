#Calculator 

from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=1)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
#e.insert(0, "Enter your calculation")

def button_click(number):
    #e.delete(0, END) -- allows one integer per click, erases previous number, not great for calculators.
    current_number = e.get()
    e.delete(0, END) 
    e.insert(0, str(current_number) + str(number))

def button_clear():
    e.delete(0, END)

def butt_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def butt_equals():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

# Create and define the buttons 
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: butt_add())
button_equals = Button(root, text="=", padx=91, pady=20, command=lambda: butt_equals())
button_erase = Button(root, text="Clear", padx=79, pady=20, command=lambda: button_clear())

#Put the buttons on the screen
button_7.grid(row = 1, column=0)
button_8.grid(row = 1, column=1)
button_9.grid(row = 1, column=2)

button_4.grid(row = 2, column=0)
button_5.grid(row = 2, column=1)
button_6.grid(row = 2, column=2)

button_1.grid(row = 3, column=0)
button_2.grid(row = 3, column=1)
button_3.grid(row = 3, column=2)

button_0.grid(row = 4, column=0)
button_add.grid(row = 5, column = 0)
button_erase.grid(row = 4, column = 1, columnspan=2)
button_equals.grid(row = 5, column = 1, columnspan=2)

#Run it on a loop! 

root.mainloop()
