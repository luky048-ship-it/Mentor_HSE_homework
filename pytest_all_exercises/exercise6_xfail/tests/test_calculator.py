import pytest
import time
import sys
import os

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract(calc):
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(-1, 1) == -2

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(0, 10) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(-4, 2) == -2
    assert calc.divide(5, 2) == 2.5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError) as exc_info:
        calc.divide(10, 0)
    assert str(exc_info.value) == "Cannot divide by zero"

@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 3, 8),
        (1, 5, 1),
        (0, 5, 0),
        (5, 0, 1),
        (-2, 3, -8),
        (2, -2, 0.25),
    ]
)
def test_power(calc, base, exponent, expected):
    assert calc.power(base, exponent) == expected

@pytest.mark.slow
def test_heavy_computation(calc):
    time.sleep(2)
    assert calc.multiply(1000, 1000) == 1000000

@pytest.mark.fast
def test_fast_operation(calc):
    assert calc.add(1, 1) == 2

@pytest.mark.skip(reason="Тест в разработке")
def test_feature_in_development(calc):
    assert calc.power(2, 2) == 4

# Тест из упражнения 6
@pytest.mark.xfail(reason="Known bug in version 1.0")
def test_known_issue(calc):
    """Тест из упражнения 6 - ожидаемо падает"""
    assert calc.subtract(10, 5) == 6  # Нарочно неправильное ожидание (должно быть 5)
