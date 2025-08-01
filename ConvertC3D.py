import tkinter as tk

def on_click():
    label.config(text="Hello, Windows!")

root = tk.Tk()
root.title("My Windows Python App")

label = tk.Label(root, text="Welcome!")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=5)

root.mainloop()