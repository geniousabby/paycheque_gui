"""
Pay cheque calculator

"""


# Import tkinter for GUI making
import tkinter as tk


# Set up the root window
root = tk.Tk()
root.title("Pay Cheque Calculator")


# Function to multiple $/hr by hours worked
def calc_pay_per_hour():
	"""
	Calculates total money

	"""
	
	pay_per_hour = entry_hrs**selected

	print(f"Pay per hour: {pay_per_hour}")


# Function for doing the calculation for percent of taxes


# Function for doing the calculation for percent of savings


# Create and place GUI widgets on a grid


# Hours worked
# Label
label_hrs = tk.Label(root, text="Hours worked: ")
label_hrs.grid(column=0, row=0)

# Entry
entry_hrs = tk.Entry(root)
entry_hrs.grid(column=1, row=0)


# Pay per hour
# Label
label_pay = tk.Label(root, text="$ per hour: ")
label_pay.grid(column=0, row=1)

# List box
spinbox = tk.Spinbox(root, from_=1, to=200)
spinbox.grid(column=1, row=1)
selected = tk.IntVar()


# Taxes
# Label
label_taxes = tk.Label(root, text="Income Tax (%): ")
label_taxes.grid(column=0, row=2)

# Radio button
r1 = tk.Radiobutton(root, text='5.60%', value=1, variable=selected)
r1.grid(column=1, row=2)

r2 = tk.Radiobutton(root, text='7.70%', value=2, variable=selected)
r2.grid(column=1, row=3)

r3 = tk.Radiobutton(root, text='10.50%', value=3, variable=selected)
r3.grid(column=1, row=4)

r4 = tk.Radiobutton(root, text='12.29%', value=4, variable=selected)
r4.grid(column=1, row=5)

r5 = tk.Radiobutton(root, text='14.70%', value=5, variable=selected)
r5.grid(column=1, row=6)


# Savings
# Label
label_savings = tk.Label(root, text="Savings (%): ")
label_savings.grid(column=0, row=7)
# scale
# Create a Scale Widget
scale_widget = tk.Scale(root, orient="horizontal", resolution=1,
						from_=0, to=100)

scale_widget.grid(column=1, row=7)


# Commute
# Label
label_commute = tk.Label(root, text="Commute: ")
label_commute.grid(column=0, row=8)
# check button

# Variables to store checkbox states (1 = checked, 0 = unchecked)
var_tutorial = tk.IntVar(value=0)
var_student = tk.IntVar(value=0)
var_courses = tk.IntVar(value=0)

# Create Checkbuttons
chk_publictransit = tk.Checkbutton(root, text="Public transit", variable=var_tutorial)
chk_car = tk.Checkbutton(root, text="Car", variable=var_student)
chk_walk = tk.Checkbutton(root, text="Walk/bike", variable=var_courses)

# Place widgets
chk_publictransit.grid(column=1, row=8)
chk_car.grid(column=1, row=9)
chk_walk.grid(column=1, row=10)


# Calculate button
button_calculate = tk.Button(root, text="Calculate",
                             command=calc)
button_calculate.grid(column=0, row=11)

label_money = tk.Label(root, text="$: ")
label_money.grid(column=1, row=11)


root.mainloop()