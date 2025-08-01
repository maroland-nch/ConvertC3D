import tkinter as tk
from viewmodels.converter_vm import ConverterViewModel

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

        # Label to display selected file status
        self.label = tk.Label(root, text="No file selected")
        self.label.pack()

        # Button to trigger C3D file selection
        self.button = tk.Button(root, text="Select C3D...", command=self.on_select_source_button)
        self.button.pack()

    def on_select_source_button(self):
        """Handle file selection and update label text."""
        path = self.vm.select_file()

        # Default message if no file is selected
        label_text = "No file selected"

        # If a file was selected, extract and display the filename
        if self.vm.get_selected_file():
            label_text = f"Selected: {path.split('/')[-1]}"

        # Update the label widget
        self.label.config(text=label_text)

def build_ui():
    """Create and return the Tkinter root window with UI initialized."""
    root = tk.Tk()
    MainWindow(root)
    return root
