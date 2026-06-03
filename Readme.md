# Open Brewery DB API Automation Framework

## Overview

This project contains automated API tests for the Open Brewery DB API using:

* Python
* Pytest
* Requests

The API was selected from the Public APIs repository:

* Open Brewery DB: https://www.openbrewerydb.org/documentation
* Public APIs Repository: https://github.com/public-apis/public-apis

## Framework Features

* API Client Layer (Service Layer Pattern)
* Reusable Pytest Fixtures
* Positive and Negative Test Scenarios
* Pytest Parameterization
* Response Schema Validation
* Performance Validation
* HTML Test Reporting
* Scalable Project Structure

---

## Project Structure

```text
api-automation/
│
├── api/
│   └── brewery_api.py
│
├── tests/
│   └── test_brewery_api.py
│
├── conftest.py
├── README.md with gif

### Install Dependencies

pip install pytest==7.4.3
pip install requests==2.31.0

---

## Running Tests

### Execute All Tests

Clone the repository--->open in any IDE like VS code/IntelliJ, run below command and checkout generated html reports.

pytest -v --html=report.html --self-contained-html


### Run Specific Test File

```bash
pytest tests/test_brewery_api.py -v
```

### Run Parameterized Tests Only

```bash
pytest -k "city" -v
```

---

## Test Execution Demo
![TestExecutionDemo](https://github.com/ather-ctrl/api-automation_Brewery/blob/65df05b1a957b60e877510a467f7dd0a5d5016d4/APItestrun.gif)


---

## Test Cases

| Test Case ID | Scenario                      | Expected Result                                            |
| ------------ | ----------------------------- | ---------------------------------------------------------- |
| TC_API_001   | Get All Breweries Status Code | Status code should be 200                                  |
| TC_API_002   | Response Is Not Empty         | Brewery list should contain records                        |
| TC_API_003   | Response Is List              | API response should be a list                              |
| TC_API_004   | Required Fields Exist         | Required brewery fields should be present and not null     |
| TC_API_005   | Search Brewery By City        | Valid brewery data should be returned for supported cities |
| TC_API_006   | Get Brewery By Valid ID       | Status code should be 200                                  |
| TC_API_007   | Get Brewery By Invalid ID     | Status code should be 404                                  |
| TC_API_008   | Response Time Validation      | Response time should be less than 2 seconds                |

---

## Validation Strategy

The following validations are implemented to ensure API quality and reliability.

| Validation Type               | Purpose                                                         |
| ----------------------------- | --------------------------------------------------------------- |
| Status Code Validation        | Verifies endpoint availability and expected HTTP response codes |
| Response Structure Validation | Ensures API contract consistency                                |
| Response Data Validation      | Confirms response contains meaningful data                      |
| Required Field Validation     | Verifies critical business fields exist in responses            |
| Search Validation             | Confirms filtering and query parameters work correctly          |
| Resource Retrieval Validation | Verifies brewery resources can be retrieved by ID               |
| Negative Validation           | Ensures proper handling of invalid requests                     |
| Performance Validation        | Detects significant response time regressions                   |

---

## Validation Examples

### Status Code Validation

```python
assert response.status_code == 200
```

### Response Structure Validation

```python
assert isinstance(response.json(), list)
```

### Required Field Validation

```python
required_fields = [
    "id",
    "name",
    "brewery_type",
    "city",
    "state"
]

for field in required_fields:
    assert field in brewery
    assert brewery[field] is not None
```

### Search Validation

```python
response = brewery_api.get_breweries_by_city("san_diego")

assert response.status_code == 200
assert len(response.json()) > 0
```

### Negative Validation

```python
response = brewery_api.get_brewery_by_id(
    "invalid-brewery-id"
)

assert response.status_code == 404
```

### Performance Validation

```python
assert response.elapsed.total_seconds() < 2
```

---

## Design Decisions

### Service Layer Pattern

All API interactions are centralized within the `BreweryAPI` client class. This improves maintainability and reduces duplication across tests.

### Reusable Request Wrapper

A generic request method is used to centralize request execution, timeout handling, and future enhancements such as logging or retries.

### Session Management

A `requests.Session()` object is used to enable connection reuse and improve test execution performance.

### Pytest Fixtures

The API client is initialized once per test session using a reusable fixture.

### Pytest Parameterization

Parameterization is used to execute the same validation logic against multiple cities while minimizing code duplication and improving test coverage.

---

