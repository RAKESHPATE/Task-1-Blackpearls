import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', 'x^y', 'M'
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(self, text=button, padx=20, pady=20, bd=8, font=('Arial', 18), command=action).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click_event(self, key):
        if key == "=":
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero is not allowed")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif key == "C":
            self.result_var.set("")
        elif key == "√":
            try:
                result = str(math.sqrt(float(self.result_var.get())))
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for square root")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif key == "x^y":
            self.result_var.set(self.result_var.get() + "**")
        elif key == "M":
            messagebox.showinfo("Info", "Memory function not implemented yet")
        else:
            self.result_var.set(self.result_var.get() + key)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

