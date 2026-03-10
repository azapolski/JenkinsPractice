from src.app.calculator import add, div
import pytest

def test_add_positive():
    assert add(2, 3) == 5

def test_div_normal():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_fail():
    assert add(2, 3) == 5