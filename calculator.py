import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Basic Calculator")

def button_click(text):
    current = result_var.get()

    if text == "=":
        try:
            result = eval(current)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif text == "C":
        result_var.set("")
    else:
        result_var.set(current + text)

result_var = tk.StringVar()
result_entry = ttk.Entry(app, textvariable=result_var, justify="right")
result_entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    ttk.Button(app, text=button, command=lambda btn=button: button_click(btn)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()


