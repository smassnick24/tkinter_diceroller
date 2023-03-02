import tkinter as tk
from dice_roll import *

root = tk.Tk()
root.geometry("1080x720")
root.config(background="#4e8bed")

dice4 = tk.Button(root, command=Roll4)
dice6 = tk.Button(root, command=Roll6)
dice8 = tk.Button(root, command=Roll8)
dice10 = tk.Button(root, command=Roll10)
dice12 = tk.Button(root, command=Roll12)
dice20 = tk.Button(root, command=Roll20)

root.mainloop()