import json
import os
import pytest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_test_data(file_name: str) -> dict:
    with open(f'{ROOT_DIR}/test_data/{file_name}.json') as data:
        return json.load(data)


@pytest.fixture
def service_table_data(request) -> str:
    return load_test_data('parabank_services')[request.param]
