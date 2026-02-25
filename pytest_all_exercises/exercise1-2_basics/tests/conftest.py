import sys
import os
import pytest

# Сначала добавляем путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Потом импортируем
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()
