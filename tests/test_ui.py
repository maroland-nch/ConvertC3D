import tkinter as tk
import pytest
from ui.main_window import build_ui

@pytest.fixture
def app():
    root = tk.Tk()
    yield root
    root.destroy()

def find_button_by_text(root, text):
    return next(
        (w for w in root.winfo_children() if isinstance(w, tk.Button) and w["text"] == text),
        None
    )


def test_select_c3d_button():
    root = build_ui()
    button = find_button_by_text(root, "Select C3D...")
    assert button is not None
    root.destroy()