#any pytest file should start with _test or end with test_
# pytest method should start with test
import pytest


@pytest.mark.smoke
def test_firstProg():
    print("first code")

@pytest.mark.smoke
@pytest.mark.skip
def test_SecondProg():
    print("second code")

@pytest.mark.xfail
def test_thirdProg():
    print("third code")