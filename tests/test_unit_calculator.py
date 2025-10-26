import pytest
from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_sub():
    calc = Calculator()
    assert calc.sub(10, 4) == 6

def test_mul():
    calc = Calculator()
    assert calc.mul(6, 7) == 42

def test_div_normal():
    calc = Calculator()
    assert calc.div(8, 2) == 4

def test_div_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.div(5, 0)