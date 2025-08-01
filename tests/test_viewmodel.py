import time
import pytest
from viewmodels.converter_vm import ConverterViewModel

TEST_FILE_PATH = "test_data/sample.c3d"
TEST_SUMMARY_DURATION = 10
TEST_CONVERSION_DURATION = 300

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

def test_cannot_summarize_empty():
    vm = ConverterViewModel()
    vm.summarize()
    assert vm.is_summary_available() is False
    assert vm.is_summary_running() is False

def test_summarize():
    vm = ConverterViewModel()
    vm.set_selected_file(TEST_FILE_PATH)
    vm.summarize()
    assert vm.is_summary_available() is False
    assert vm.is_summary_running() is True

    for attempt in range(TEST_SUMMARY_DURATION * 2):
        if vm.is_summary_running() is False:
            break
        time.sleep(0.5)
    
    assert vm.is_summary_running() is False
    assert vm.is_summary_available() is True

def test_cannot_convert_empty():
    vm = ConverterViewModel()
    vm.convert()
    assert vm.is_conversion_running() is False

def test_conversion_starts():
    vm = ConverterViewModel()
    vm.set_selected_file(TEST_FILE_PATH)
    assert vm.get_selected_file() == TEST_FILE_PATH
    
    vm.convert()
    assert vm.is_conversion_running() is True

def test_conversion():
    vm = ConverterViewModel()
    vm.set_selected_file(TEST_FILE_PATH)
    assert vm.get_selected_file() == TEST_FILE_PATH

    vm.convert()
    assert vm.is_conversion_available() is False
    assert vm.is_conversion_running() is True

    for attempt in range(TEST_CONVERSION_DURATION * 2):
        if vm.is_conversion_running() is False:
            break
        time.sleep(0.5)
    
    assert vm.is_conversion_running() is False
    assert vm.is_conversion_available() is True
    assert vm.is_conversion_successful() is True
