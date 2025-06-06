import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from calculator import binary_converter


def test_correct_conversion():
    assert binary_converter.to_binary(5) == "101"
    assert binary_converter.to_binary(10) == "1010"
    assert binary_converter.to_binary(1) == "1"
    assert binary_converter.to_binary(2) == "10"
    assert binary_converter.to_binary(100) == "1100100"


def test_out_of_range():
    with pytest.raises(ValueError):
        binary_converter.to_binary(-1)
    with pytest.raises(ValueError):
        binary_converter.to_binary(256)


def test_non_integer_input():
    with pytest.raises(TypeError):
        binary_converter.to_binary("10.0")
    with pytest.raises(TypeError):
        binary_converter.to_binary(10.0)
    with pytest.raises(TypeError):
        binary_converter.to_binary(3.14)
