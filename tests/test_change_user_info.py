import allure
import pytest

from helper import generate_user_body
from methods.user_methods import UserMethods


class TestChangeUserInfo:
    @allure.title('Успешное изменение имени/пароля/емейла у авторизованного пользователя')
    @pytest.mark.parametrize("key", ['name', 'password', 'email'])
    def test_change_auth_user_info(self, generate_user_data, key):
        response_headers = generate_user_data['auth_headers']
        second_user_data = generate_user_body()
        new_user_data = {
            "name": generate_user_data['name'],
            "password": generate_user_data['password'],
            "email": generate_user_data['email']
        }
        new_user_data[key] = second_user_data[key]
        response = UserMethods.change_user_info(body=new_user_data, headers=response_headers)
        response_data = response.json()
        assert response.status_code == 200 and "success" in response_data

    @allure.title('Получение ошибки при изменении имени/пароля/емейла у неавторизованного пользователя')
    @pytest.mark.parametrize("key", ['name', 'password', 'email'])
    def test_change_not_auth_user_info(self, generate_user_data, key):
        second_user_data = generate_user_body()
        new_user_data = {
            "email": generate_user_data['email'],
            "password": generate_user_data['password'],
            "name": generate_user_data['name']
        }
        new_user_data[key] = second_user_data[key]
        response = UserMethods.change_user_info_without_auth(body=new_user_data)
        response_data = response.json()
        expected_response = {
            "success": False,
            "message": "You should be authorised"
        }
        assert response.status_code == 401 and response_data == expected_response
