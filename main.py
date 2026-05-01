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
label_mass = tk.Label(root, text="Savings (%): ")
label_mass.grid(column=0, row=7)
# scale
# Create a Scale Widget
scale_widget = tk.Scale(root, orient="horizontal", resolution=1,
                        from_=0, to=100)

scale_widget.grid(column=1, row=7)


# Commute
# Label
label_mass = tk.Label(root, text="Commute: ")
label_mass.grid(column=0, row=8)
# check button

# Variables to store checkbox states (1 = checked, 0 = unchecked)
var_tutorial = tk.IntVar(value=0)
var_student = tk.IntVar(value=0)
var_courses = tk.IntVar(value=0)

# Create Checkbuttons
chk_tutorial = tk.Checkbutton(root, text="Public transit", variable=var_tutorial)
chk_student = tk.Checkbutton(root, text="Car", variable=var_student)
chk_courses = tk.Checkbutton(root, text="Walk/bike", variable=var_courses)

# Place widgets
chk_tutorial.grid(column=1, row=8)
chk_student.grid(column=1, row=9)
chk_courses.grid(column=1, row=10)


# Calculate button


root.mainloop()