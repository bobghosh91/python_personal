import pytest

@pytest.mark.usefixtures("setup")
class TestExample_methods:

    def test_demo1(self):
        print("print demo1")

    def test_demo2(self):
        print("print demo2")

    def test_demo3(self):
        print(" print demo3")
