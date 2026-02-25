import sys
import os
import pytest

# Добавляем родительскую директорию в путь Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()
