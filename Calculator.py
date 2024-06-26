#Calculator 

from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap('GUIProjects/calc_icon.png')

# This is the "Screen" of your calculator that shows the numbers you choose
e = Entry(root, width=35, borderwidth=1)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
#e.insert(0, "Enter your calculation") - If you wanted text overlay on the "screen" 

#This function puts the number you click on the screen of your calculator 
def button_click(number):
    current_number = e.get()
    e.delete(0, END) 
    e.insert(0, str(current_number) + str(number))

# Clear the calculator
def clear():
    e.delete(0, END)

# This stores your first number clicked on and prepares it for the equal function
def addition():
    first_number = e.get()
    global f_num
    global math
    math = "addition" 
    f_num = int(first_number)
    e.delete(0, END)

def subtract(): 
    first_number = e.get()
    global f_num
    global math
    math = "subtraction" 
    f_num = int(first_number)
    e.delete(0, END)

def multiply(): 
    first_number = e.get()
    global f_num
    global math
    math = "multiplication" 
    f_num = int(first_number)
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num
    global math
    math = "division" 
    f_num = int(first_number)
    e.delete(0, END)

# Takes the first number using the global variable f_num and adds it to the second_number after clicking "+"
def equals():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))

# Create and define the buttons 
# The format goes like this: Button(root directory, text to go on the button, size of the buttons, how they should function if clicked on)
button_1 = Button(root, text="1", padx=42, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: addition())
button_subtract = Button(root, text="-", padx=39, pady=20, fg="orange", command=lambda: subtract())
button_multiply = Button(root, text="X", padx=39, pady=20, fg="orange", command=lambda: multiply())
button_divide = Button(root, text="/", padx=42, pady=20, fg="orange", command=lambda: divide())
button_equals = Button(root, text="=", padx=165, pady=20, command=lambda: equals())
button_erase = Button(root, text="Clear", padx=91, pady=20, command=lambda: clear())
button_quit = Button(root, text="Exit", padx=39, pady=20, fg="red", command=root.quit)

# Put the buttons on the screen in order they should show up on the calculator 
button_7.grid(row = 1, column=0)
button_8.grid(row = 1, column=1)
button_9.grid(row = 1, column=2)
button_multiply.grid(row = 1, column = 3)

button_4.grid(row = 2, column=0)
button_5.grid(row = 2, column=1)
button_6.grid(row = 2, column=2)
button_subtract.grid(row=2, column=3)

button_1.grid(row = 3, column=0)
button_2.grid(row = 3, column=1)
button_3.grid(row = 3, column=2)
button_divide.grid(row=3, column=3)

button_0.grid(row = 4, column=0)
button_erase.grid(row = 4, column = 1, columnspan=2)
button_add.grid(row = 4, column = 3)

button_quit.grid(row=5, column=3)
button_equals.grid(row = 5, column = 0, columnspan=3)


#Run the program continuously until closed 
root.mainloop()
