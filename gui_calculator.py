"""
GUI Calculator using Tkinter.

This GUI uses the functions defined in calculator.py:
- add(x, y)
- subtract(x, y)
- multiply(x, y)
- divide(x, y)
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Import the calculation functions from your existing calculator.py
from calculator import add, subtract, multiply, divide


class CalculatorGUI:
    """A simple GUI wrapper around the basic calculator functions."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Simple Calculator (GUI)")
        self.root.resizable(False, False)

        # Main frame
        main_frame = ttk.Frame(self.root, padding="16")
        main_frame.grid(row=0, column=0, sticky="NSEW")

        # Number 1 label + entry
        ttk.Label(main_frame, text="First number:").grid(row=0, column=0, sticky="W")
        self.entry_num1 = ttk.Entry(main_frame, width=20)
        self.entry_num1.grid(row=0, column=1, padx=(8, 0), pady=4)

        # Number 2 label + entry
        ttk.Label(main_frame, text="Second number:").grid(row=1, column=0, sticky="W")
        self.entry_num2 = ttk.Entry(main_frame, width=20)
        self.entry_num2.grid(row=1, column=1, padx=(8, 0), pady=4)

        # Operation selection
        ttk.Label(main_frame, text="Operation:").grid(row=2, column=0, sticky="W", pady=(8, 4))
        self.operation_var = tk.StringVar(value="add")

        operations = [
            ("Add (+)", "add"),
            ("Subtract (-)", "subtract"),
            ("Multiply (×)", "multiply"),
            ("Divide (÷)", "divide"),
        ]

        op_frame = ttk.Frame(main_frame)
        op_frame.grid(row=2, column=1, sticky="W")

        for text, value in operations:
            ttk.Radiobutton(
                op_frame,
                text=text,
                value=value,
                variable=self.operation_var
            ).pack(anchor="w")

        # Calculate button
        calc_button = ttk.Button(main_frame, text="Calculate", command=self.calculate)
        calc_button.grid(row=3, column=0, columnspan=2, pady=(12, 8), sticky="EW")

        # Result label
        self.result_label = ttk.Label(main_frame, text="Result: ", font=("Segoe UI", 10, "bold"))
        self.result_label.grid(row=4, column=0, columnspan=2, sticky="W", pady=(4, 0))

    def calculate(self) -> None:
        """Read inputs, perform calculation, and update the result label."""
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers.")
            return

        operation = self.operation_var.get()

        try:
            if operation == "add":
                result = add(num1, num2)
                symbol = "+"
            elif operation == "subtract":
                result = subtract(num1, num2)
                symbol = "-"
            elif operation == "multiply":
                result = multiply(num1, num2)
                symbol = "×"
            elif operation == "divide":
                result = divide(num1, num2)
                symbol = "÷"
            else:
                messagebox.showerror("Error", "Unknown operation selected.")
                return

            self.result_label.config(
                text=f"Result: {num1} {symbol} {num2} = {result}"
            )

        except ZeroDivisionError:
            messagebox.showerror("Math error", "Cannot divide by zero.")
            self.result_label.config(text="Result: Error")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop() 
