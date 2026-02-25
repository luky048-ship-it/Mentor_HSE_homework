import pytest
import time

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
    time.sleep(2)  # Симуляция долгой операции (2 секунды вместо 5)
    assert calc.multiply(1000, 1000) == 1000000

@pytest.mark.fast
def test_fast_operation(calc):
    """Быстрый тест - помечен как fast"""
    assert calc.add(1, 1) == 2

@pytest.mark.slow
def test_another_slow_computation(calc):
    """Еще один медленный тест"""
    time.sleep(1)
    result = 0
    for i in range(10000):
        result += calc.add(i, i)
    assert result == 99990000

@pytest.mark.skip(reason="Тест в разработке, еще не готов")
def test_feature_in_development(calc):
    """Пропущенный тест - помечен как skip"""
    assert calc.power(2, 2) == 4  # Этот тест не будет запускаться

import sys

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Требуется Python 3.8 или выше")
def test_python_version_specific(calc):
    """Тест работает только на Python 3.8+"""
    assert calc.power(3, 2) == 9

@pytest.mark.xfail(reason="Известная проблема, которую еще не исправили")
def test_known_issue(calc):
    """Тест, который ожидаемо падает"""
    # Этот тест должен упасть, и это нормально
    assert calc.divide(1, 3) == 0.3333333333333333  # Проблема с точностью float
