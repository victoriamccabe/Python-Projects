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
        self.source_dir = Entry(self.master, width=80)
        # Positions entry in GUI using tkinter grid() padx and pady are
        # the same as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, padx=(20,10), pady=(30,0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(self.master, text="Select Destination", width=20, command=self.destDir)
        # Positions entry in GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,0))

        # Creates entry for destination directory selection
        self.dest_dir = Entry(self.master, width=80)
        # Positions entry in GUI using tkinter grid()
        # padx and pady are the same as the button to ensure they line up
        self.dest_dir.grid(row=1, column=1, padx=(20,10), pady=(15,0))

        # Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(0,20), pady=(15,15))

        # Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # Positions the Exit button
        self.exit_btn.grid(row=2, column=1, padx=(20,10), pady=(15,15), sticky='e')

        # Label to show source directory last modified time
        self.source_time_label = tk.Label(self.master, text="", fg="red")
        self.source_time_label.grid(row=0, column=2, padx=(20,10), pady=(30,0))

        # Label to show destination directory last modified time
        self.dest_time_label = tk.Label(self.master, text="", fg="red")
        self.dest_time_label.grid(row=1, column=2, padx=(20,10), pady=(15,0))

        # Text widget to display transfer status messages
        self.msg_box = tk.Text(self.master, height=2, width=83)
        self.msg_box.grid(row=3, column=0, columnspan=3, padx=(20,0), pady=(0,30), sticky='w')
        # Start as read-only
        self.msg_box.config(state=tk.DISABLED)  
    


            
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

        now = datetime.datetime.now().timestamp()
        # Clear previous messages and prepare to display new ones
        self.msg_box.config(state=tk.NORMAL)
        self.msg_box.delete('1.0', tk.END)

        # For each selected file, check if modified in last 24 hours and display last modified time
        for file_path in self.selected_files:
            file_mtime = os.path.getmtime(file_path)
            time_diff = now - file_mtime
            if time_diff < 24 * 60 * 60:
                mod_time_str = datetime.datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')
                self.msg_box.insert(tk.END, f"{os.path.basename(file_path)} - Last modified: {mod_time_str}\n")

        self.msg_box.config(state=tk.DISABLED)

        
        
    # Creates function to select destination directory
    def destDir(self):
        selectDestDir = filedialog.askdirectory()
        # Clears existing content in the entry
        self.dest_dir.delete(0, END)
        # Inserts the selected path into the entry
        self.dest_dir.insert(0, selectDestDir)

        

    # Creates function to exit program
    def exit_program(self):
        # Root is the main GUI window, the Tkinter destroy method
        # tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


    def transferFiles(self):
        destination = self.dest_dir.get()
        now = datetime.datetime.now().timestamp()

        self.msg_box.config(state=tk.NORMAL)
        self.msg_box.delete('1.0', tk.END)

        for file_path in self.selected_files:
            file_mtime = os.path.getmtime(file_path)
            time_diff = now - file_mtime

            if time_diff < 24 * 60 * 60:
                filename = os.path.basename(file_path)
                # Format last modified time nicely
                mod_time_str = datetime.datetime.fromtimestamp(file_mtime).strftime('%Y-%m-%d %H:%M:%S')
                
                shutil.move(file_path, os.path.join(destination, filename))
                self.msg_box.insert(tk.END, f"{filename} was successfully transferred. Last modified: {mod_time_str}\n")

        self.msg_box.config(state=tk.DISABLED)



                
# Main application launcher
if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
