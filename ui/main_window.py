import tkinter as tk
from viewmodels.converter_vm import ConverterViewModel

DELTATIME = 250 #millis

INSTRUCTIONS = "Please select a C3D file to analyze. \nClick 'Summarize' to pull metadata about the animation\nClick 'Convert' to convert to .fbx"
LABEL_SELECT_BLANK = "No C3D file selected"
LABEL_CONVERSION_IN_PROGRESS = ""
LABEL_SUMMARY_IN_PROGRESS = ""

class MainWindow:
    """Main UI window for the Mocap Converter application.

    This class builds the UI and handles interactions like selecting a C3D file
    and displaying the selected file path.
    """

    def __init__(self, root):
        """Initialize the main window and its widgets."""
        self.root = root
        self.vm = ConverterViewModel()

        # Set window title and size
        self.root.title("Mocap Converter")
        self.root.geometry("300x400")

        #Text to display instructions
        self.instructions = tk.Label(root, text=INSTRUCTIONS)
        self.instructions.pack(pady=10)

        # Label to display selected file status
        self.label = tk.Label(root, text="No file selected")
        self.label.pack(pady=10)

        # Button to trigger C3D file selection
        self.select_button = tk.Button(root, text="Select C3D...", command=self.on_select_source_button)
        self.select_button.pack()

        # Button to trigger summary
        self.summary_button = tk.Button(root, text="Summarize", command=self.on_summarize_button)
        self.summary_button.config(state="disabled")
        self.summary_button.pack()

        # Button to trigger conversion
        self.convert_button = tk.Button(root, text="Convert", command=self.on_convert_button)
        self.convert_button.config(state="disabled")
        self.convert_button.pack()


    def update(self):
        """Do any necessary UI updates here."""
        # Selected button label
        selected = self.vm.get_selected_file()
        if selected is None:
            selected = LABEL_SELECT_BLANK

        self.label.config(text=selected)

        #Disable buttons while in progress
        allow_buttons = "disabled"
        if self.get_are_buttons_allowed():
            allow_buttons = "normal"

        self.select_button.config(state=allow_buttons)
        self.convert_button.config(state=allow_buttons)
        self.summary_button.config(state=allow_buttons)

    def on_select_source_button(self):
        """Handle file selection and update label text."""
        path = self.vm.select_file()

        # Default message if no file is selected
        label_text = "No file selected"

        # If a file was selected, extract and display the filename
        if self.vm.get_selected_file():
            label_text = f"Selected: {path.split('/')[-1]}"
        else:
            label_text = LABEL_SELECT_BLANK

        # Update the UI
        self.label.config(text=label_text)
        self.schedule_update()
    
    def on_summarize_button(self):
        if self.get_is_summary_startable():
            self.vm.summarize()
        self.schedule_update()

    def on_convert_button(self):
        if self.get_is_convert_startable():
            self.schedule_update()
        self.schedule_update()

    def is_update_pending(self):
        """ Checks if work in progress will need a UI refresh down the line """
        if self.vm is None:
            return False
        
        if self.vm.is_conversion_running():
            return True
        if self.vm.is_summary_running():
            return True
        
        return False

    def schedule_update(self):
        """ Recursive call to update UI until work is completed """
        self.update()
        if self.is_update_pending():
            self.root.after(DELTATIME, self.schedule_update)

    def get_is_summary_startable(self):
        if self.vm is None:
            return False
        if self.vm.get_selected_file() is None:
            return False
        if self.vm.is_summary_running():
            return False
        return True
    
    def get_is_convert_startable(self):
        if self.vm is None:
            return False
        if self.vm.get_selected_file() is None:
            return False
        if self.vm.is_summary_running():
            return False
        if self.vm.is_conversion_running():
            return False
        return True
    
    def get_are_buttons_allowed(self):
        return self.get_is_convert_startable() and self.get_is_summary_startable()

def build_ui():
    """Create and return the Tkinter root window with UI initialized."""
    root = tk.Tk()
    MainWindow(root)
    return root