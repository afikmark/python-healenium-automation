from assertpy import assert_that
from forms.pet_store.user import CreateUser
import pytest


@pytest.mark.sanity
def test_create_user(pet_store_api):
    create_user_params = CreateUser(id=0,
                                    username="John",
                                    firstName="John",
                                    lastName="Demo",
                                    email="JohnDemo@gmail.com",
                                    password="test_password",
                                    phone="000000000",
                                    user_status=0)
    response = pet_store_api.create_user(create_user_params)
    assert_that(response.status_code, 'status code').is_equal_to(200)


@pytest.mark.sanity
def test_login(pet_store_api):
    response = pet_store_api.login(username="John", password='Demo')
    assert_that(response.status_code, 'status code').is_equal_to(200)
