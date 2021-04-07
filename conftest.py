import pytest

from olek.api import OlekAPI


@pytest.fixture
def api():
    return OlekAPI()


@pytest.fixture
def client(api):
    return api.test_session()
