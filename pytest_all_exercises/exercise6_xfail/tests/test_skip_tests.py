import sys
import pytest

class TestSkipConditions:
    
    @pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
    def test_specific_platform(self, calc):
        """Тест из упражнения 5"""
        assert calc.divide(10, 2) == 5
    
    @pytest.mark.skipif(sys.platform != "linux", reason="Только для Linux")
    def test_linux_only(self, calc):
        """Тест только для Linux"""
        assert calc.add(1, 1) == 2
    
    @pytest.mark.skipif(sys.version_info < (3, 8), reason="Требуется Python 3.8+")
    def test_python_38_plus(self, calc):
        """Тест для Python 3.8 и выше"""
        assert calc.multiply(3, 3) == 9
