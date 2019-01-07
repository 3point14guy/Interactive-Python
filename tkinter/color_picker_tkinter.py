#Not working

# import tkinter as tk
# from tkinter import colorchooser
## colorpicker window doesn't open and program freezes

from tkinter import *

application_window = Tk()

rgb_color, web_color = colorchooser.askcolor(parent=application_window, initialcolor=(255, 0, 0))

application_window.mainloop()


# import tkinter as tk
# import tkinter.ttk as ttk
# from tkcolorpicker import askcolor
## error ModuleNotFoundError: No module named 'tkcolorpicker'

# root = tk.Tk()
# style = ttk.Style(root)
# style.theme_use('clam')
#
# print(askcolor((255, 255, 0), root))
# root.mainloop()
