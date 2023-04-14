import pytest


@pytest.mark.usefixtures("setup")
class TestExamples:

    def test_example_01(self):
        print("I am a testcase")
    
    def test_example_02(self):
        print("I am second test case")


