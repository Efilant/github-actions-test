"""
Basit bir hesap makinesi modülü
"""


def add(a, b):
    """İki sayıyı toplar"""
    return a + b


def subtract(a, b):
    """İki sayıyı çıkarır"""
    return a - b


def multiply(a, b):
    """İki sayıyı çarpar"""
    return a * b


def divide(a, b):
    """İki sayıyı böler"""
    if b == 0:
        raise ValueError("Sıfıra bölme hatası!")
    return a / b

