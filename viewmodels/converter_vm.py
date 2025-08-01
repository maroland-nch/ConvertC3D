from tkinter import filedialog
from models.fbx_converter import FbxConverter
from models.summary_converter import SummaryConverter

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
        if not self.active_converter is None:
            return
        
        if self.selected_file is None:
            return
        
        self.active_converter = FbxConverter()
        self.active_converter.initialize(self.select_file)
        self.active_converter.start()
    
    def is_conversion_running(self):
        """ Check if a conversion operation is running """
        if self.active_converter is None:
            return False
        
        return self.active_converter.is_running()
    
    def is_conversion_available(self):
        """ Check if converted data was successfully generated"""
        if self.active_converter is None:
            return False
        
        return self.active_converter.is_result_available()
    
    def is_conversion_successful(self):
        """ Check if the last conversion operation was successful """
        if self.active_converter is None:
            return False
        
        return self.active_converter.is_successful()
    
    def summarize(self):
        """ Begin the process of summarizing the source c3d file, if one is selected """
        if not self.active_summary_parser is None:
            return
        
        if self.selected_file is None:
            return
        
        self.active_summary_parser = SummaryConverter()
        self.active_summary_parser.initialize(self.select_file)
        self.active_summary_parser.start()

    def is_summary_running(self):
        """ Check if a summary parse operation is in progress """
        if self.active_summary_parser is None:
            return False
        
        return self.active_summary_parser.is_running()
    
    def is_summary_available(self):
        """ Check if summary data is parsed and available """
        return self.summary is not None


