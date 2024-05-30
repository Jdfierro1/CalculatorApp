from tkinter import * 

root = Tk()

# Step 1: Create the things 
#myLabel1 = Label(root, text="This is my first GUI Project!").grid(row=0, column=3)
#### ^^^^ Notice how you can add .grid(row, column) at the end of the variable being created 
#myLabel2 = Label(root, text="Let's make Friday Jr!")
#myLabel3 = Label(root, text="Lets get centered")
#myLabel4 = Label(root, text="Last row")

# Entry widget allows for user input: 
e = Entry(root, width = 50, fg="blue", borderwidth=1)
e.insert(0, "Project Updates: ")


# Creating buttons: 
def myClick():
    Saved = f"{e.get()}"
    myLabel = Label(root, text=Saved)
    myLabel.pack()
myButton = Button(root, text="Save your updates", padx=30, pady=10, command=myClick) #fg="green", bg="red"
# padx/pady changes the size of the button



# Step 2: Put things on the screen using the grid system, or pack
#myLabel2.grid(row=1, column=5)
#myLabel3.grid(row=2, column=10)
#myLabel4.grid(row=10, column=5)
e.pack()
myButton.pack(side="bottom")


# Notes to think about: 
# myLabel.pack() --- The .pack() method is similar to packing a suitcase. Shoves it in, it's fixed


root.mainloop()