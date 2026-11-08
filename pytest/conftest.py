import pytest

@pytest.fixture(scope="session")
def preSetUpWork():
    print("\n\n//////////////////////////////////////// test start //////////////////////////////////////////")
    print("Browser Instance scope=session")
