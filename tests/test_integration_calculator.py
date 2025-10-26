import pytest
from src.calculator import Calculator

def complex_calculation(a, b, c, d, e):
    """
    Több lépéses folyamat:
    1. (a + b)
    2. eredmény * c
    3. eredmény / d
    4. eredmény - e
    Több calculator metódust együtt.
    """
    calc = Calculator()

    step1 = calc.add(a, b)      # (a + b)
    step2 = calc.mul(step1, c)  # (a + b) * c
    step3 = calc.div(step2, d)  # ((a + b) * c) / d
    step4 = calc.sub(step3, e)  # ((a + b) * c / d) - e
    return step4

def test_complex_calculation_happy_path():
    result = complex_calculation(a=2, b=3, c=4, d=5, e=1)
    # ellenőrzés kézzel:
    # a+b = 5
    # 5*4 = 20
    # 20/5 = 4
    # 4-1 = 3
    assert result == 3

def test_complex_calculation_div_zero():
    # itt várom, hogy hibát kapjak, mert d=0, és a div() hibát dob 0-val osztásnál
    with pytest.raises(ValueError):
        complex_calculation(a=1, b=2, c=3, d=0, e=10)