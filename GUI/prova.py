
import tkinter as tk


###########################################################

def handle_keypress(event):
    print("Hello World!")

##########################################################
#MAIN

window = tk.Tk()

#greeting = tk.Label(text="Hello, Tkinter")
#greeting.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()

button.bind("<Button-1>", handle_keypress)

window.mainloop()