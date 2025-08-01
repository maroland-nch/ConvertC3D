from tkinter import filedialog
from models.converter import convert_c3d_to_fbx

class ConverterViewModel:
    def __init__(self):
        """Initialize viewmodel state."""
        self.selected_file = None
        self.active_converter = None
        self.active_summary_parser = None
        self.summary = None
        self.converted = None

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
    
    def convert(self):
        """ Begin the process of converting the file, if one is selected"""
        # Placeholder
        if self.active_converter is None:
            self.active_converter = 1 
            self.converted = None
        else:
            self.active_converter = None
            self.converted = "Placeholder conversion"
    
    def is_conversion_running(self):
        """ Check if a conversion operation is running """
        return self.active_converter is not None
    
    def is_conversion_available(self):
        """ Check if converted data was successfully generated"""
        return self.converted is not None
    
    def is_conversion_successful(self):
        """ Check if the last conversion operation was successful """
        return self.converted is not None
    
    def summarize(self):
        """ Begin the process of summarizing the source c3d file, if one is selected """
        # Placeholder
        if self.active_summary_parser is None:
            self.summary is None
            self.active_summary_parser = 1 
        else:
            self.active_summary_parser = None
            self.summary = "Placeholder summary"

    def is_summary_running(self):
        """ Check if a summary parse operation is in progress """
        return self.active_summary_parser is not None
    
    def is_summary_available(self):
        """ Check if summary data is parsed and available """
        return self.summary is not None


