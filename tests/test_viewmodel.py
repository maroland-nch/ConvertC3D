import pytest
from viewmodels.converter_vm import ConverterViewModel

def test_initial_state():
    vm = ConverterViewModel()
    assert vm.get_selected_file() is None
    assert vm.is_conversion_running() is False

def test_set_and_get_selected_file():
    vm = ConverterViewModel()
    vm.set_selected_file("test_file.c3d")
    assert vm.get_selected_file() == "test_file.c3d"

def test_set_selected_file_ignores_empty():
    vm = ConverterViewModel()
    vm.set_selected_file("") 
    # Empty path should be ignored
    assert vm.get_selected_file() is None

    vm.set_selected_file("test_file.c3d")
    vm.set_selected_file("")
    # Empty path should leave stored path unchanged
    assert vm.get_selected_file() == "test_file.c3d" 

