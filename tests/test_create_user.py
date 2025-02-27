import allure
import pytest
import requests

from helper import generate_user_body
from methods.user_methods import UserMethods
from tests.conftest import generate_user_data


class TestCreateUser:
    @allure.title('Успешное создание нового пользователя с передачей всех обязательных полей')
    def test_create_unic_user(self):
        user_data = generate_user_body()
        response = UserMethods.create_user(user_data)
        response_status_code = response.status_code
        response_body = response.json()
        access_token = response.json().get("accessToken")
        assert response_status_code == 200 and "success" in response_body
        auth_headers = {
            'Authorization': access_token
        }
        UserMethods.delete_user(auth_headers)

    @allure.title('Получение ошибки при создании пользователя, который уже был ранее создан')
    def test_create_user_twice(self, generate_user_data):
        response_first_status_code = generate_user_data['create_status_code']
        response_first_data = generate_user_data['create_body']
        response_second = UserMethods.create_user({
            "email": generate_user_data['email'],
            "password": generate_user_data['password'],
            "name": generate_user_data['name']
        })
        response_second_data = response_second.json()
        expected_second_response = {
            "success": False,
            "message": "User already exists"
        }
        assert response_first_status_code == 200 and "success" in response_first_data
        assert response_second.status_code == 403 and response_second_data == expected_second_response

    @allure.title('Получение ошибки при создании пользователя без заполнения обязательного поля имейл/имя/пароль')
    @pytest.mark.parametrize("key", ['name', 'password', 'email'])
    def test_create_user_without_necessary_info(self, key):
        user_data = generate_user_body()
        del user_data [key]
        response = UserMethods.create_user(user_data)
        response_data = response.json()
        expected_response = {
        "success": False,
        "message": "Email, password and name are required fields"
        }
        assert response.status_code == 403 and response_data == expected_response
