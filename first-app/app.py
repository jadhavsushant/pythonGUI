import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

label = tk.Label(text="Hello, Tkinter", fg="yellow", bg="#34A2FE")


entry = tk.Entry(fg="yellow", bg="blue", width=50,)

button = tk.Button(text="click back",
                   fg="red",
                   bg="yellow",
                   height=10,
                   width=10)
print(entry.get())

label.pack()
entry.pack()
button.pack()

root.mainloop()
