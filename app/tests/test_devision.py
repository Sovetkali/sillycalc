import pytest
from app.main import division


def test_division():
    assert division(1, 2) == 0.5


def test_zero_division():
    with pytest.raises(ValueError, match=r".* by zero"):
        division(2, 0)
