import pytest


@pytest.mark.smoke
def test_first_program():
    print("Hello World")


def test_second_program():
    print("Olala")
    msg = "Some message"
    assert "Some" in msg, "Mesage do not match with pattern."


@pytest.fixture()
def setup():
    print("I will run first")



def test_demo_fixture(setup):
    print("I will execute after setup")
    