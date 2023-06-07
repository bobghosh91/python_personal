import pytest

@pytest.fixture() #scope="class" add this if we want only to run befoe class and after
def setup():
    print("i will run first")
    yield
    print("i will run last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Bob","ghosh","abc@gmail.com"]
@pytest.fixture(params=["chrome", "Firefox", "Edge"])
def crossBrowser(request):
    return request.param
