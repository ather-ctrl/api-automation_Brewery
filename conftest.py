import pytest
from api.brewery_api import BreweryAPI


@pytest.fixture(scope="session")
def brewery_api():
    """
    API client fixture.
    """
    return BreweryAPI()