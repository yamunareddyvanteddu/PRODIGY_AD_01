import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")

# Entry widget to display input and results
entry = tk.Entry(app, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

# Define buttons and their placement
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(app, text=button, width=5, height=2,
              command=lambda btn=button: on_click(btn) if btn != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(app, text='C', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val, columnspan=2)

# Run the application
app.mainloop()
