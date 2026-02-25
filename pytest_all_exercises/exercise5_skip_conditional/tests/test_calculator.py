import pytest
import time
import sys
import os  # Добавляем импорт os

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

@pytest.mark.skipif(sys.version_info < (3, 7), reason="Требуется Python 3.7 или выше")
def test_python_version_check(calc):
    """Тест только для Python 3.7+"""
    assert calc.power(2, 10) == 1024

@pytest.mark.skipif(sys.platform != "linux", reason="Только для Linux")
def test_linux_only(calc):
    """Тест только для Linux систем"""
    assert calc.multiply(3, 4) == 12

@pytest.mark.skipif(sys.platform == "darwin", reason="Не работает на macOS")
def test_not_for_mac(calc):
    """Тест, который пропускается на macOS"""
    assert calc.add(5, 3) == 8

# Тест с несколькими условиями
@pytest.mark.skipif(
    sys.platform == "win32" or sys.version_info < (3, 8),
    reason="Требуется не-Windows и Python >= 3.8"
)
def test_multiple_conditions(calc):
    """Тест с несколькими условиями пропуска"""
    assert calc.subtract(20, 10) == 10

def test_platform_specific_logic(calc):
    """Тест с логикой внутри, зависящей от платформы"""
    if sys.platform == "win32":
        # Windows-специфичная логика
        result = calc.divide(100, 10)
    else:
        # Unix-специфичная логика
        result = calc.divide(100, 5)
    
    # Разные ожидания для разных платформ
    if sys.platform == "win32":
        assert result == 10
    else:
        assert result == 20

try:
    import numpy
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

@pytest.mark.skipif(not HAS_NUMPY, reason="Требуется numpy")
def test_with_optional_dependency(calc):
    """Тест, который работает только если установлен numpy"""
    import numpy as np
    # Используем numpy для вычислений
    np_result = np.array([calc.add(1, 2), calc.multiply(3, 4)])
    assert list(np_result) == [3, 12]

# Тест с пользовательским условием
IS_CI = os.environ.get('CI', 'false').lower() == 'true'

@pytest.mark.skipif(IS_CI, reason="Не запускать в CI окружении")
def test_skip_in_ci(calc):
    """Тест, который пропускается в CI окружении"""
    assert calc.power(3, 3) == 27
