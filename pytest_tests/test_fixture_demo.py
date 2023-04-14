import pytest


@pytest.fixture()
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


def test_demo_01(setup):
    print("I will execute after setup. ")

