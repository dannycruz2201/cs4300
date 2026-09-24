import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task1 import hello_world

def test_hello_world(capsys):
    # Call the function that prints text
    hello_world("Hello World")

    # Capture stdout and stderr
    captured = capsys.readouterr()

    # Verify the output by using the assert statement
    assert captured.out == "Hello World\n"