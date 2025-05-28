import tkinter as tk
from tkinter import filedialog

def browse_file1():
    file_path = filedialog.askopenfilename()
    entry1.delete(0, tk.END)
    entry1.insert(0, file_path)

def browse_file2():
    file_path = filedialog.askopenfilename()
    entry2.delete(0, tk.END)
    entry2.insert(0, file_path)

def check_files():
    # Placeholder for file checking logic
    print("Checking files...")

def close_program():
    root.destroy()

def select_directory():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print(f"Selected folder: {folder_path}")
        # You can also display it in a Label or Entry if needed

# Main window
root = tk.Tk()
root.title("Check files")
root.geometry("400x130")
root.resizable(False, False)

# Row 1
browse_button1 = tk.Button(root, text="Browse...", width=10, command=browse_file1)
browse_button1.grid(row=0, column=0, padx=10, pady=5)

entry1 = tk.Entry(root, width=40)
entry1.grid(row=0, column=1, padx=10, pady=5)

# Row 2
browse_button2 = tk.Button(root, text="Browse...", width=10, command=browse_file2)
browse_button2.grid(row=1, column=0, padx=10, pady=5)

entry2 = tk.Entry(root, width=40)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Row 3
check_button = tk.Button(root, text="Check for files...", width=15, command=check_files)
check_button.grid(row=2, column=0, padx=10, pady=10)

close_button = tk.Button(root, text="Close Program", width=15, command=close_program)
close_button.grid(row=2, column=1, sticky='e', padx=10, pady=10)

# Optional: Add a button to test directory selection
select_dir_button = tk.Button(root, text="Select Folder", command=select_directory)
select_dir_button.place(x=155, y=100)  # Adjust position as needed

root.mainloop()


