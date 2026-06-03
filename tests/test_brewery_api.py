import pytest

        # https://www.openbrewerydb.org/documentation
        # this is taken from https://github.com/public-apis/public-apis
class TestBreweryAPI:

    REQUIRED_FIELDS = [
        "id",
        "name",
        "brewery_type",
        "city",
        "state"
    ]

    def test_get_breweries_status_code(self, brewery_api):
        """
        TC_API_001
        Verify breweries endpoint is accessible.
        """
        response = brewery_api.get_all_breweries()

        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_response_is_not_empty(self, brewery_api):
        """
        TC_API_002
        Verify breweries list contains data.
        """
        response = brewery_api.get_all_breweries()

        assert len(response.json()) > 0, \
            "Expected brewery list to contain records"

    def test_response_is_list(self, brewery_api):
        """
        TC_API_003
        Verify API returns list.
        """
        response = brewery_api.get_all_breweries()

        assert isinstance(response.json(), list), \
            "Response is not a list"

    def test_required_fields_exist(self, brewery_api):
        """
        TC_API_004
        Verify mandatory fields exist.
        """
        response = brewery_api.get_all_breweries()

        brewery = response.json()[0]

        for field in self.REQUIRED_FIELDS:
            assert field in brewery, \
                f"Missing field: {field}"

            assert brewery[field] is not None, \
                f"{field} should not be None"
    #Parameterization is used here recommended.
    @pytest.mark.parametrize(
        "city",
        [
            "san_diego",
            "new_york",
            "austin"
        ]
    )
    def test_search_by_city(self, brewery_api, city):
        """
        TC_API_005
        Verify city search works.
        """
        response = brewery_api.get_breweries_by_city(city)

        assert response.status_code == 200

        breweries = response.json()

        assert isinstance(breweries, list)

        assert len(breweries) > 0

    @pytest.mark.parametrize(
        "brewery_id, expected_status",
        [
            (
                "5128df48-79fc-4f0f-8b52-d06be54d0cec",
                200
            ),
            (
                "invalid-brewery-id",
                404
            )
        ]
    )
    def test_get_brewery_by_id(
            self,
            brewery_api,
            brewery_id,
            expected_status):
        """
        TC_API_006
        TC_API_007
        Verify brewery lookup by ID.
        """
        response = brewery_api.get_brewery_by_id(
            brewery_id
        )

        assert response.status_code == expected_status

    def test_response_time_under_two_seconds(
            self,
            brewery_api):
        """
        TC_API_008
        Verify response time.
        """
        response = brewery_api.get_all_breweries()
        assert response.elapsed.total_seconds() < 2, \
            f"Response took {response.elapsed.total_seconds()} seconds"