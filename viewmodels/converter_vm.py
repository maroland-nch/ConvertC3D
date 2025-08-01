from tkinter import filedialog
from models.converter import convert_c3d_to_fbx

class ConverterViewModel:
    def __init__(self):
        """Initialize viewmodel state."""
        self.selected_file = None
        self.active_converter = None

    def select_file(self):
        """Open file dialog and store selected C3D file path."""
        path = filedialog.askopenfilename(filetypes=[("C3D files", "*.c3d")])
        self.set_selected_file(path)
        return self.get_selected_file()

    def get_selected_file(self):
        """Return the stored C3D file path."""
        return self.selected_file

    def set_selected_file(self, path):
        """Store C3D file path."""
        if path:
            self.selected_file = path
    
    def is_conversion_running(self):
        return self.active_converter is not None

