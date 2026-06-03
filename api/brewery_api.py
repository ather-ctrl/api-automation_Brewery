import requests

        # https://www.openbrewerydb.org/documentation

class BreweryAPI:
    """
    Client for Open Brewery DB APIs.
    """

    BASE_URL = "https://api.openbrewerydb.org/v1/breweries"
    TIMEOUT = 10

    def __init__(self):
        self.session = requests.Session()

    def _get(self, endpoint="", params=None):
        """
        Generic GET request wrapper.
        """
        return self.session.get(
            f"{self.BASE_URL}{endpoint}",
            params=params,
            timeout=self.TIMEOUT
        )

    def get_all_breweries(self):
        return self._get()

    def get_breweries_by_city(self, city):
        return self._get(
            params={"by_city": city}
        )

    def get_brewery_by_id(self, brewery_id):
        return self._get(
            f"/{brewery_id}"
        )