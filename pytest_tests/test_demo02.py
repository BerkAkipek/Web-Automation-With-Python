import pytest


@pytest.mark.skip
def test_first_program():
    msg = "Hello World"
    assert msg == "Hello", "Strings do not match"


def test_second_program(setup):
    a, b = 4, 6
    assert a+2 == b, "Addition do not match."


def test_third_program(setup):
    a = 4 / 2
    assert type(a) is float, "a has to be a float"

