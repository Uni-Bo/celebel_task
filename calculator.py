import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math

# Create the main window
window = tk.Tk()
window.title('Simple Calculator')

# Set the frame background color using a hex value
frame = tk.Frame(master=window, bg="#0f591c", padx=10)  # Hex color for light blue
frame.pack()

# Create an entry widget for displaying the input and output
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

# Function to handle button clicks and insert the number/operator into the entry widget
def myclick(number):
    entry.insert(tk.END, number)

# Function to evaluate the expression entered in the entry widget
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Function to compute power
def power():
    try:
        base, exponent = entry.get().split('^')
        result = str(pow(float(base), float(exponent)))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

# Function to compute square root
def sqrt():
    try:
        number = float(entry.get())
        result = str(math.sqrt(number))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

class RoundedButton(tk.Canvas):
    def __init__(self, master, text, command, radius=15, padding=5, bg="#000000", fg="#ffffff", font=("Helvetica", 12), *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.command = command
        self.radius = radius
        self.padding = padding
        self.bg = bg
        self.fg = fg
        self.font = font
        self.width = radius * 2 + padding * 2
        self.height = radius * 2 + padding * 2
        self.configure(width=self.width, height=self.height, bg=self.bg, highlightthickness=0)
        
        self.create_oval((padding, padding, padding + radius * 2, padding + radius * 2), fill=self.bg, outline=self.bg)
        self.create_oval((padding, padding, padding + radius * 2, padding + radius * 2), fill=self.bg, outline=self.bg)
        self.create_rectangle((padding, padding + radius, padding + radius * 2, padding + radius), fill=self.bg, outline=self.bg)
        self.create_rectangle((padding + radius, padding, padding + radius, padding + radius * 2), fill=self.bg, outline=self.bg)
        
        self.text_id = self.create_text((self.width // 2, self.height // 2), text=text, fill=self.fg, font=self.font)
        self.bind("<Button-1>", self._on_click)
        
    def _on_click(self, event):
        if self.command:
            self.command()

# Creating buttons for numbers 0-9 and placing them in the grid
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1)
]

for (text, row, col) in buttons:
    button = RoundedButton(master=frame, text=text, radius=15, padding=5, command=lambda t=text: myclick(t), bg="#4CAF50", fg="#ffffff")
    button.grid(row=row, column=col, pady=2)

# Creating buttons for operators and other functionalities
operators = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('^', 5, 0), ('sqrt', 5, 1), ('clear', 5, 2), ('=', 5, 3)
]

for operator in operators:
    if operator[0] == 'clear':
        button = RoundedButton(master=frame, text=operator[0], radius=15, padding=5, command=clear, bg="#f44336", fg="#ffffff")
        button.grid(row=operator[1], column=operator[2], pady=2)
    elif operator[0] == '=':
        button = RoundedButton(master=frame, text=operator[0], radius=15, padding=5, command=equal, bg="#2196F3", fg="#ffffff")
        button.grid(row=operator[1], column=operator[2], pady=2)
    elif operator[0] == '^':
        button = RoundedButton(master=frame, text=operator[0], radius=15, padding=5, command=lambda: myclick('^'), bg="#FF9800", fg="#ffffff")
        button.grid(row=operator[1], column=operator[2], pady=2)
    elif operator[0] == 'sqrt':
        button = RoundedButton(master=frame, text=operator[0], radius=15, padding=5, command=sqrt, bg="#FF9800", fg="#ffffff")
        button.grid(row=operator[1], column=operator[2], pady=2)
    else:
        button = RoundedButton(master=frame, text=operator[0], radius=15, padding=5, command=lambda o=operator[0]: myclick(o), bg="#4CAF50", fg="#ffffff")
        button.grid(row=operator[1], column=operator[2], pady=2)

# Start the main loop to run the application
window.mainloop()
