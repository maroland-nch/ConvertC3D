import tkinter as tk

def build_ui():
    #Initialize window
    root = tk.Tk()
    root.title("Mocap Converter")
    root.geometry("400x300")

    #Initialize viewmodels

    #Pack elements
    button = tk.Button(root, text = "Select C3D...")
    button.pack(pady=20)

    return root
