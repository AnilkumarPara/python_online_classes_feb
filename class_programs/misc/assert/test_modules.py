import pytest


def even(n):
    return n % 2 == 0


def test_even():
    assert even(2), "Odd number"
