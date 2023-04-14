# I am a special script. fixtures which defined in this file can be used by any test case in this file. 
import pytest


@pytest.fixture(scope="class")
def setup():
    print("I can be called from outside. ")
    yield
    print("I am after yield")


@pytest.fixture()
def data_load():
    return ["Berk", "Akipek", "example@example.com"]


@pytest.fixture(params=[("chrome", "berk", "akipek"), "firefox", "iexplorer"])
def cross_browser(request):
    return request.param

