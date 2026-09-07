'''GUI Calculator (Simple, Loan, SGPA to %)'''

import tkinter as tk
from tkinter import messagebox, ttk

# ------SIMPLE CALCULATOR-----------
calc_expression = ""

def append_to_display(value):
    global calc_expression
    calc_expression += str(value)
    calc_display.delete(0, tk.END)
    calc_display.insert(0, calc_expression)

def calculate_simple():
    global calc_expression
    try:
        result = eval(calc_expression)
        calc_display.delete(0, tk.END)
        calc_display.insert(0, str(result))
        calc_expression = str(result)
    except:
        calc_display.delete(0, tk.END)
        calc_display.insert(0, "Error")
        calc_expression = ""

def clear_simple():
    global calc_expression
    calc_expression = ""
    calc_display.delete(0, tk.END)

def backspace_simple():
    global calc_expression
    # Remove the last character from the string
    calc_expression = calc_expression[:-1]
    calc_display.delete(0, tk.END)
    calc_display.insert(0, calc_expression)


# ------LOAN CALCULATOR------
def calculate_loan():
    try:
        principal = float(principal_entry.get())
        annual_rate = float(rate_entry.get()) / 100
        years = int(years_entry.get())

        if principal <= 0 or annual_rate < 0 or years <= 0:
            raise ValueError("Values must be positive.")

        monthly_rate = annual_rate / 12
        num_payments = years * 12

        if monthly_rate == 0:
            monthly_payment = principal / num_payments
        else:
            monthly_payment = (
                principal
                * (monthly_rate * (1 + monthly_rate) ** num_payments)
                / ((1 + monthly_rate) ** num_payments - 1)
            )

        total_payment = monthly_payment * num_payments
        total_interest = total_payment - principal

        loan_result_label.config(
            text=f"Monthly Payment: ₹{monthly_payment:.2f}\n"
            f"Total Payment: ₹{total_payment:.2f}\n"
            f"Total Interest: ₹{total_interest:.2f}"
        )

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


# ------SGPA TO % CONVERTER------
def calculate_percentage():
    try:
        sgpa = float(entry_sgpa.get())
        if sgpa < 0 or sgpa > 10:
            messagebox.showerror("Error", "SGPA must be between 0 and 10.")
            return

        percentage = sgpa * 10
        sgpa_result_label.config(text=f"Percentage: {percentage:.2f}%")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric SGPA.")


# MAIN APPLICATION WINDOW
root = tk.Tk()
root.title("Multi-Utility Calculator Suite")
root.geometry("460x500")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Simple Calculator")
notebook.add(tab2, text="Loan Calculator")
notebook.add(tab3, text="SGPA Converter")

# TAB 1: SIMPLE CALCULATOR UI
calc_display = tk.Entry(tab1, font=("Arial", 20), justify="right")
calc_display.grid(
    row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew"
)

buttons = [
    "C", "⌫", "/", "*", "7", "8", "9", "-", "4", "5", "6", "+", "1", "2", "3", "=", "0", ".",
]

row_idx = 1
col_idx = 0
for btn in buttons:
    if btn == "=":
        tk.Button(
            tab1, text=btn, font=("Arial", 16), command=calculate_simple
        ).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")
    elif btn == "C":
        tk.Button(
            tab1, text=btn, font=("Arial", 16), command=clear_simple
        ).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")
    elif btn == "⌫":
        tk.Button(
            tab1, text=btn, font=("Arial", 16), command=backspace_simple
        ).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(
            tab1,
            text=btn,
            font=("Arial", 16),
            command=lambda b=btn: append_to_display(b),
        ).grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")

    col_idx += 1
    if col_idx > 3:
        col_idx = 0
        row_idx += 1

for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
for i in range(4):
    tab1.grid_columnconfigure(i, weight=1)

# TAB 2: LOAN CALCULATOR UI
tk.Label(tab2, text="Principal Amount (₹):", font=("Arial", 12)).grid(
    row=0, column=0, padx=15, pady=15, sticky="w"
)
principal_entry = tk.Entry(tab2, font=("Arial", 12))
principal_entry.grid(row=0, column=1, padx=15, pady=15)

tk.Label(tab2, text="Annual Interest Rate (%):", font=("Arial", 12)).grid(
    row=1, column=0, padx=15, pady=15, sticky="w"
)
rate_entry = tk.Entry(tab2, font=("Arial", 12))
rate_entry.grid(row=1, column=1, padx=15, pady=15)

tk.Label(tab2, text="Loan Term (Years):", font=("Arial", 12)).grid(
    row=2, column=0, padx=15, pady=15, sticky="w"
)
years_entry = tk.Entry(tab2, font=("Arial", 12))
years_entry.grid(row=2, column=1, padx=15, pady=15)

calculate_button = tk.Button(
    tab2, text="Calculate", font=("Arial", 14, "bold"), command=calculate_loan
)
calculate_button.grid(row=3, column=0, columnspan=2, pady=15)

loan_result_label = tk.Label(tab2, text="", font=("Arial", 12))
loan_result_label.grid(row=4, column=0, columnspan=2, pady=10)

# TAB 3: SGPA CONVERTER UI
LABEL_FONT = ("Arial", 15)
ENTRY_FONT = ("Arial", 16)
BUTTON_FONT = ("Arial", 12)
RESULT_FONT = ("Arial", 13)

label_instruction = tk.Label(tab3, text="Enter SGPA (0-10):", font=LABEL_FONT)
label_instruction.grid(row=0, column=0, padx=15, pady=30, sticky="w")

entry_sgpa = tk.Entry(tab3, font=ENTRY_FONT, width=18)
entry_sgpa.grid(row=0, column=1, padx=15, pady=30)

button_calculate = tk.Button(
    tab3,
    text="Calculate Percentage",
    font=BUTTON_FONT,
    command=calculate_percentage,
    fg="black",
)
button_calculate.grid(row=1, column=0, columnspan=2, pady=20)

sgpa_result_label = tk.Label(tab3, text="Percentage: ", font=RESULT_FONT)
sgpa_result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()