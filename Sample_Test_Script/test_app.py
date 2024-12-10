# test_app.py
import pytest

def test_add():
    assert 2 + 3 == 5
    assert -1 + 1 == 0
    assert 1 + 1 == 2
    a,b,c = 1,2,3
    assert a + b == c
    # assert 1 + 2 == 4 # Faulty
    assert 0 + 0 == 0

def test_subtract():
    assert 5 - 2 == 3
    assert 3 - 3 == 0
    assert 2 - 4 == -2

if __name__ == "__main__":
    pytest.main()
