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
label_mass = tk.Label(root, text="Wage per hour: ")
label_mass.grid(column=0, row=1)

# Radio button
selected = tk.IntVar()

r1 = tk.Radiobutton(root, text='$15', value=1, variable=selected)
r1.grid(column=1, row=1)

r2 = tk.Radiobutton(root, text='$20', value=2, variable=selected)
r2.grid(column=1, row=2)

r3 = tk.Radiobutton(root, text='$30', value=3, variable=selected)
r3.grid(column=1, row=3)

r4 = tk.Radiobutton(root, text='$50', value=4, variable=selected)
r4.grid(column=1, row=4)

r5 = tk.Radiobutton(root, text='$75', value=5, variable=selected)
r5.grid(column=1, row=5)

r6 = tk.Radiobutton(root, text='$100', value=6, variable=selected)
r6.grid(column=1, row=6)


# Taxes
# Label
# List box


# Savings
# Label
# scale


# Commute
# Label
# check button


# Calculate button


root.mainloop()