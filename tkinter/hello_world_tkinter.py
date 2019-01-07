import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

window = tk.Tk()

# my_label = ttk.Label(window, text="Hello World!")
# my_label.grid(row=1, column=1)

# messagebox.showinfo("Information", "Information Message")
# messagebox.showerror("Error", "My error message")
# messagebox.showwarning("WARNING!", "Warning message")

# answer = messagebox.askokcancel("QUESTION", "DO YOU WANT TO OPEN A FILE?")
# answer = messagebox.askretrycancel("Question", "Do you want to try again?")
# answer = messagebox.askyesno("Question", "Do you like Python?")
# answer = messagebox.askyesnocancel("Hey You!", "Continue playing?")

answer = simpledialog.askstring("input", "WHat is your first name?", parent=window)

if answer is not None:
    print("Hello ", answer)
else:
    print("hello annonymous user")

answer = simpledialog.askinteger("input", "What is your age", parent=window, minvalue=0, maxvalue=100)

if answer is not None:
    my_label = ttk.Label(window, text="Wow, I am {} too!".format(answer))
    my_label.grid(row=10, column=20)
else:
    my_label = ttk.Label(window, text="Most people who feel old won't enter their age either.")
    my_label.grid(row=10, column=20)

window.mainloop()
