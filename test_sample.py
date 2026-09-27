import random

def test_stable():
    assert 1 + 1 == 2

def test_flaky():
    assert random.random() > 0.5
