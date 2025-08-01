import tkinter as tk
from viewmodels.converter_vm import ConverterViewModel

def run_app():
    root = tk.Tk()
    root.title("C3D to FBX")

    vm = ConverterViewModel()

    btn = tk.Button(root, text="Convert", command=vm.select_and_convert)
    btn.pack(pady=20)

    root.mainloop()
