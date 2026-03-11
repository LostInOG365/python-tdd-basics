from rechner import addition

def test_addition_positiv():
    assert addition(2, 3) == 5

def test_addition_negativ():
    assert addition(-1, -4) == -5

def test_addition_null():
    assert addition(0, 0) == 0

from rechner import addition, division

def test_division_normal():
    assert division(10, 2) == 5

def test_division_durch_null():
    # Wir erwarten eine Exception
    import pytest
    with pytest.raises(ValueError):
        division(10, 0)