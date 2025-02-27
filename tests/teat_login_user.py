import allure

from helper import generate_user_body
from methods.user_methods import UserMethods


class TestLoginUser:
    @allure.title('Успешная авторизация созданного пользователя')
    def test_login_user(self):
        user_data = generate_user_body()
        UserMethods.create_user(user_data)
        login_payload = {
            "email": user_data['email'],
            "password": user_data['password'],
            "name": user_data['name']
        }
        login_response = UserMethods.login_user(login_payload)
        login_response_status_code = login_response.status_code
        login_response_body = login_response.json()
        access_token = login_response.json().get("accessToken")
        assert login_response_status_code == 200 and "success" in login_response_body
        auth_headers = {
            'Authorization': access_token
        }
        UserMethods.delete_user(auth_headers)

    @allure.title('Получение ошибки при вводе авторизации с некорректным имейлом и паролем')
    def test_login_user_with_wrong_email_and_password(self, generate_user_data):
        second_user_data = generate_user_body()
        wrong_user_data = {
            "email": second_user_data['email'],
            "password": second_user_data['password']
        }
        response = UserMethods.login_user(wrong_user_data)
        response_data = response.json()
        expected_response = {
        "success": False,
        "message": "email or password are incorrect"
        }
        assert response.status_code == 401 and response_data == expected_response


