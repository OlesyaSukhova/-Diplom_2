import allure

from helper import generate_user_body
from methods.user_methods import UserMethods


class TestChangeUserInfo:
    @allure.title('Успешное изменение имени у авторизованного пользователя')
    def test_change_auth_user_name(self, generate_user_data):
        response_headers = generate_user_data['auth_headers']
        second_user_data = generate_user_body()
        new_user_data = {
            "email": generate_user_data['email'],
            "password": generate_user_data['password'],
            "name": second_user_data['name']
        }
        response = UserMethods.change_user_info(body=new_user_data, headers=response_headers)
        response_data = response.json()
        assert response.status_code == 200 and "success" in response_data

    @allure.title('Успешное изменение имейла у авторизованного пользователя')
    def test_change_auth_user_email(self, generate_user_data):
        response_headers = generate_user_data['auth_headers']
        second_user_data = generate_user_body()
        new_user_data = {
            "email": second_user_data['email'],
            "password": generate_user_data['password'],
            "name": generate_user_data['name']
        }
        response = UserMethods.change_user_info(body=new_user_data, headers=response_headers)
        response_data = response.json()
        assert response.status_code == 200 and "success" in response_data

    @allure.title('Успешное изменение пароля у авторизованного пользователя')
    def test_change_auth_user_password(self, generate_user_data):
        response_headers = generate_user_data['auth_headers']
        second_user_data = generate_user_body()
        new_user_data = {
            "email": generate_user_data['email'],
            "password": second_user_data['password'],
            "name": generate_user_data['name']
        }
        response = UserMethods.change_user_info(body=new_user_data, headers=response_headers)
        response_data = response.json()
        assert response.status_code == 200 and "success" in response_data

    @allure.title('Получение ошибки при изменении имени у неавторизованного пользователя')
    def test_change_not_auth_user_name(self, generate_user_data):
        second_user_data = generate_user_body()
        new_user_data = {
            "email": generate_user_data['email'],
            "password": generate_user_data['password'],
            "name": second_user_data['name']
        }
        response = UserMethods.change_user_info_without_auth(body=new_user_data)
        response_data = response.json()
        expected_response = {
            "success": False,
            "message": "You should be authorised"
        }
        assert response.status_code == 401 and response_data == expected_response

    @allure.title('Получение ошибки при изменении имейл у неавторизованного пользователя')
    def test_change_not_auth_user_email(self, generate_user_data):
        second_user_data = generate_user_body()
        new_user_data = {
            "email": second_user_data['email'],
            "password": generate_user_data['password'],
            "name": generate_user_data['name']
        }
        response = UserMethods.change_user_info_without_auth(body=new_user_data)
        response_data = response.json()
        expected_response = {
            "success": False,
            "message": "You should be authorised"
        }
        assert response.status_code == 401 and response_data == expected_response

    @allure.title('Получение ошибки при изменении пароля у неавторизованного пользователя')
    def test_change_not_auth_user_password(self, generate_user_data):
        second_user_data = generate_user_body()
        new_user_data = {
            "email": generate_user_data['email'],
            "password": second_user_data['password'],
            "name": generate_user_data['name']
        }
        response = UserMethods.change_user_info_without_auth(body=new_user_data)
        response_data = response.json()
        expected_response = {
            "success": False,
            "message": "You should be authorised"
        }
        assert response.status_code == 401 and response_data == expected_response





