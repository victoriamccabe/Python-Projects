import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import shutil
import datetime


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # Sets title of GUI window
        self.master.title("File Transfer")

        # Stores list of selected files
        self.selected_files = []

        # Creates a button to select files from source directory
        self.sourceDir_btn = Button(self.master, text="Select Files", width=20, command=self.sourceDir)
        # Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        # Creates entry for source file selection
        self.source_dir = Entry(self.master, width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are
        # the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, padx=(20,10), pady=(30,0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(self.master, text="Select Destination", width=20, command=self.destDir)
        # Positions entry in GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,0))

        # Creates entry for destination directory selection
        self.dest_dir = Entry(self.master, width=75)
        # Positions entry in GUI using tkinter grid()
        # padx and pady are the same as the button to ensure they line up
        self.dest_dir.grid(row=1, column=1, padx=(20,10), pady=(15,0))

        # Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        # Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

        # Label to show source directory last modified time
        self.source_time_label = tk.Label(self.master, text="", fg="red")
        self.source_time_label.grid(row=0, column=2, padx=(20,10), pady=(30,0))

        # Label to show destination directory last modified time
        self.dest_time_label = tk.Label(self.master, text="", fg="red")
        self.dest_time_label.grid(row=1, column=2, padx=(20,10), pady=(15,0))

    



            
    # Creates function to select source files
    def sourceDir(self):
        file_paths = filedialog.askopenfilenames()
        # Store selected file paths
        self.selected_files = list(file_paths)
        # The .delete(0,END) will clear the content that is inserted in the Entry widget,
        # this allows the paths to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection (file names only) into the source_dir Entry
        file_names = [os.path.basename(f) for f in self.selected_files]
        self.source_dir.insert(0, "; ".join(file_names))

        # Check if the user has selected at least one file
        if self.selected_files:
            # Get the directory of the first selected file
            source_dir = os.path.dirname(self.selected_files[0])
            
            # Check if the directory exists
            if os.path.exists(source_dir):
                # Get the last modified timestamp of the directory (in seconds since epoch)
                mod_time = os.path.getmtime(source_dir)
                
                # Convert the timestamp into a readable datetime format
                formatted_time = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
                
                # Update the label on the GUI to display the last modified time
                self.source_time_label.config(text=f"Last modified: {formatted_time}")
            else:
                # If the directory doesn't exist, show an error message on the label
                self.source_time_label.config(text="Directory not found.")

        
    # Creates function to select destination directory
    def destDir(self):
        selectDestDir = filedialog.askdirectory()
        # Clears existing content in the entry
        self.dest_dir.delete(0, END)
        # Inserts the selected path into the entry
        self.dest_dir.insert(0, selectDestDir)

        # Get and display last modified time
        if os.path.exists(selectDestDir):
            # Get the last modified timestamp of the selected destination directory (in seconds since epoch)
            mod_time = os.path.getmtime(selectDestDir)
            
            # Convert the timestamp into a readable datetime format
            formatted_time = datetime.datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
            
            # Update the label on the GUI to display the last modified time
            self.dest_time_label.config(text=f"Last modified: {formatted_time}")
        else:
            # If the directory doesn't exist, show an error message on the label
            self.dest_time_label.config(text="Directory not found.")



    # Creates function to exit program
    def exit_program(self):
        # Root is the main GUI window, the Tkinter destroy method
        # tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

    # Creates function to transfer files from one directory to another
    def transferFiles(self):
        # Gets destination directory
        destination = self.dest_dir.get()
        # Runs through each selected file
        for file_path in self.selected_files:
            # Gets the file name from the full path
            filename = os.path.basename(file_path)
            # Moves each file from the source to the destination
            shutil.move(file_path, os.path.join(destination, filename))
            print(filename + ' was successfully transferred.')

# Main application launcher
if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
