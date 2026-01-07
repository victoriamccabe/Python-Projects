# Importing tkinter module and all of its contents
import tkinter
from tkinter import *

# Define a class that inherits from tkinter's Frame class
class ParentWindow(Frame):
    def __init__(self, master):
        # Call the constructor of the parent Frame class
        Frame.__init__(self)

        # Store a reference to the main window
        self.master = master

        # Make the main window resizable
        self.master.resizable(width=True, height=True)

        # Set the dimensions of the window (width x height)
        self.master.geometry('{}x{}'.format(700, 400))

        # Set the title of the window
        self.master.title('Learning Tkinter!')

        # Set the background color of the window
        self.master.config(bg='lightgray')

        # Create StringVar() instances to store user input from Entry widgets
        self.varFName = StringVar()
        self.varLName = StringVar()

        # Create and place a label for "First Name"
        self.lblFName = Label(self.master, text='First Name:', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        # Create and place a label for "Last Name"
        self.lblLName = Label(self.master, text='Last Name:', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))

        # Create and place an initially empty label to display a message after submission
        self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))

        # Create and place an Entry widget for first name input
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))

        # Create and place an Entry widget for last name input
        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))

        # Create and place a "Submit" button; triggers self.submit when clicked
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE)

        # Create and place a "Cancel" button; triggers self.cancel when clicked
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0, 90), pady=(30, 0), sticky=NE)

    # This method is executed when the Submit button is clicked
    def submit(self):
        # Retrieve values from Entry fields
        fn = self.varFName.get()
        ln = self.varLName.get()
        
        # Display a greeting message with the entered first and last names
        self.lblDisplay.config(text="Hello {} {}!".format(fn, ln))

    # This method is executed when the Cancel button is clicked
    def cancel(self):
        # Closes the application by destroying the main window
        self.master.destroy()

# Main program entry point
if __name__ == "__main__":
    # Create the main window object
    root = Tk()

    # Instantiate the ParentWindow class, passing the root window
    App = ParentWindow(root)

    # Start the Tkinter event loop to keep the window open
    root.mainloop()
