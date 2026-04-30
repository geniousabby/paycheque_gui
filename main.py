"""
Pay cheque calculator

"""


# Import tkinter for GUI making
import tkinter as tk


# Set up the root window
root = tk.Tk()
root.title("Pay cheque calculator")


# Function for doing the calculation for percent of taxes


# Function for doing the calculation for percent of savings


# Create and place GUI widgets on a grid


# Hours worked
# Label
label_mass = tk.Label(root, text="Hours worked: ")
label_mass.grid(column=0, row=0)

# Entry
entry_mass = tk.Entry(root)
entry_mass.grid(column=1, row=0)


# Pay per hour
# Label
label_mass = tk.Label(root, text="$ per hour: ")
label_mass.grid(column=0, row=1)

# List box
spinbox = tk.Spinbox(root, from_=1, to=200)
spinbox.grid(column=1, row=1)
selected = tk.IntVar()



# Taxes
# Label
label_mass = tk.Label(root, text="Income Tax (%): ")
label_mass.grid(column=0, row=2)

# Radio button
r1 = tk.Radiobutton(root, text='5.60%', value=1, variable=selected)
r1.grid(column=1, row=2)

r1 = tk.Radiobutton(root, text='7.70%', value=1, variable=selected)
r1.grid(column=1, row=3)

r1 = tk.Radiobutton(root, text='10.50%', value=1, variable=selected)
r1.grid(column=1, row=4)

r1 = tk.Radiobutton(root, text='12.29%', value=1, variable=selected)
r1.grid(column=1, row=5)

r1 = tk.Radiobutton(root, text='14.70%', value=1, variable=selected)
r1.grid(column=1, row=6)


# Savings
# Label
# scale


# Commute
# Label
# check button


# Calculate button


root.mainloop()