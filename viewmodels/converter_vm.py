from tkinter import filedialog
from models.converter import convert_c3d_to_fbx

class ConverterViewModel:
    def select_and_convert(self):
        path = filedialog.askopenfilename()
        if path:
            convert_c3d_to_fbx(path)
