class ApiValidations:
    #utlity
    @staticmethod
    def validate_status_code(response, expected):
        assert response.status_code == expected, \
            f"Expected {expected} but got {response.status_code}"

    @staticmethod
    def validate_response_not_empty(response):
        assert len(response.json()) > 0, \
            "Response body is empty"