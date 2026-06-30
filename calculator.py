import tkinter as tk
from tkinter import ttk


def on_button_click(text):
    if text == 'C':
        entry_var.set('')
    elif text == '=':
        try:
            value = eval(entry_var.get())
            entry_var.set(str(value))
        except Exception:
            entry_var.set('Error')
    else:
        entry_var.set(entry_var.get() + text)


def create_calculator():
    root = tk.Tk()
    root.title('Calculator')
    root.resizable(False, False)

    global entry_var
    entry_var = tk.StringVar()

    entry = ttk.Entry(root, textvariable=entry_var, font=('Segoe UI', 18), justify='right')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '=', '+'],
    ]

    for row_index, row_values in enumerate(buttons, start=1):
        for col_index, label in enumerate(row_values):
            button = ttk.Button(root, text=label, command=lambda value=label: on_button_click(value))
            button.grid(row=row_index, column=col_index, ipadx=10, ipady=10, padx=5, pady=5, sticky='nsew')

    clear_button = ttk.Button(root, text='C', command=lambda: on_button_click('C'))
    clear_button.grid(row=5, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

    for i in range(4):
        root.grid_columnconfigure(i, weight=1)
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)

    root.mainloop()


if __name__ == '__main__':
    create_calculator()
