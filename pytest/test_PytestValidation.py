import pytest

@pytest.fixture(scope="module")
def preWork():
    print("\n\n//////////////////////////////////////// test start //////////////////////////////////////////")
    print("Browser Instance scope=function")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("\n\n//////////////////////////////////////// test start //////////////////////////////////////////")
    print("Browser Instance scope=function")
    yield
    print("tear down validation")

@pytest.mark.smoke
def test_initialCheck(preWork,secondWork):
    print("Initial Check")
    assert preWork == "pass"

@pytest.mark.skip(reason="skip")
def test_thirdCheck(preSetUpWork):
    print("Third Check")