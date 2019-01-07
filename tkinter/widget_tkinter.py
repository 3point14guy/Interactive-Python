import tkinter as tk
from tkinter import ttk

app_window = tk.Tk()
frame = tk.Frame(app_window)
frame.pack()

cmd_button1 = tk.Button(frame, text="Example1")
cmd_button1.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)

# cmd_button1.pack(side=tk.TOP)
cmd_button2 = ttk.Button(frame, text="Example2")
# cmd_button2.grid(row=1, column=3, sticky=tk.N + tk.S, ipady=10)
cmd_button2.pack(side=tk.TOP, fill=tk.Y, expand=True, pady=10)
# cmd_button2.pack(side=tk.RIGHT)

app_window.mainloop()
