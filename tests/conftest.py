import pytest
import requests

from helper import Url, generate_user_body
from methods.user_methods import UserMethods


@pytest.fixture(scope='function')
def user_methods():
    return UserMethods()

@pytest.fixture(scope='function')
def generate_user_data():
    user_data = generate_user_body()
    response = UserMethods.create_user(user_data)
    response_status_code = response.status_code
    response_body = response.json()

    login_payload = {
        "email": user_data['email'],
        "password": user_data['password'],
        "name": user_data['name']

    }
    login_response = requests.post(f'{Url.base_url}{Url.login_user}', json=login_payload)
    login_response_status_code = login_response.status_code
    login_response_body = login_response.json()
    access_token = login_response.json().get("accessToken")
    auth_headers = {
        'Authorization': access_token
    }

    yield {
        "create_status_code": response_status_code,
        "create_body": response_body,
        "access_token": access_token,
        "email": user_data['email'],
        "password": user_data['password'],
        "name": user_data['name'],
        "login_status_code": login_response_status_code,
        "login_body": login_response_body,
        "auth_headers": auth_headers
    }
    requests.delete(f'{Url.base_url}{Url.user_info}', headers=auth_headers)