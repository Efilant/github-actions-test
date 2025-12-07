"""
Basit birim testleri - Her zaman başarılı olacak testler
"""
import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    """Toplama işlemi testi"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Çıkarma işlemi testi"""
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5


def test_multiply():
    """Çarpma işlemi testi"""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    """Bölme işlemi testi"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(1, 1) == 1


def test_divide_by_zero():
    """Sıfıra bölme hatası testi"""
    with pytest.raises(ValueError):
        divide(10, 0)


def test_failing_test():
    """Bu test başarısız olacak - ekran görüntüsü için"""
    assert add(2, 2) == 5  # Bu yanlış, test başarısız olacak

