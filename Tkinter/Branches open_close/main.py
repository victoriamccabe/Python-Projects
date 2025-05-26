from tkinter import *
import tkinter as tk
import Time_func

root = tk.Tk()
root.title("Branch Time Compare")

# Create top labels
lbCity = Label(root, text="City")
lbTime = Label(root, text="Time")
lbOpen = Label(root, text="Status")  # Updated label for open/closed status

# Create branch labels
bra1 = Label(root, text="Portland")
bra2 = Label(root, text="NYC")
bra3 = Label(root, text="London")

# Create time labels for each city
time_por = Label(root, text="")
time_nyc = Label(root, text="")
time_lon = Label(root, text="")

# Create status labels for each city
status_por = Label(root, text="")
status_nyc = Label(root, text="")
status_lon = Label(root, text="")

# Position the labels
lbCity.grid(row=1, column=0, padx=10, pady=5)
lbTime.grid(row=1, column=1, padx=10, pady=5)
lbOpen.grid(row=1, column=2, padx=10, pady=5)

bra1.grid(row=2, column=0, padx=10, pady=5, sticky='w')
bra2.grid(row=3, column=0, padx=10, pady=5, sticky='w')
bra3.grid(row=4, column=0, padx=10, pady=5, sticky='w')

time_por.grid(row=2, column=1, padx=10, pady=5)
time_nyc.grid(row=3, column=1, padx=10, pady=5)
time_lon.grid(row=4, column=1, padx=10, pady=5)

status_por.grid(row=2, column=2, padx=10, pady=5)
status_nyc.grid(row=3, column=2, padx=10, pady=5)
status_lon.grid(row=4, column=2, padx=10, pady=5)

# Function to update times and open/closed status
def update_times():
    # Update times
    time_por.config(text=Time_func.get_time_portland())
    time_nyc.config(text=Time_func.get_time_nyc())
    time_lon.config(text=Time_func.get_time_london())

    # Update open/closed status
    status_por.config(text=Time_func.is_branch_open("America/Los_Angeles"))
    status_nyc.config(text=Time_func.is_branch_open("America/New_York"))
    status_lon.config(text=Time_func.is_branch_open("Europe/London"))

    # Schedule next update in 1 second
    root.after(1000, update_times)

update_times()  # start the updates

root.mainloop()
