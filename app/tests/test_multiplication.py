from app.main import multiplication


def test_multiplication():
    assert multiplication(2, 3) == 6


def test_multiplication_by_zero():
    assert multiplication(2, 0) == 0
