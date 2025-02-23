import allure

from data import ingredients, ingredients_2
from methods.user_methods import UserMethods


class TestMakeAnOrder:
    @allure.title('Успешное создание заказа авторизованного пользователя с передачей ингридиентов')
    def test_make_an_order_auth_user(self, generate_user_data):
        response_headers = generate_user_data['auth_headers']
        response = UserMethods.make_an_order(body=ingredients, headers=response_headers)
        response_data = response.json()
        assert response.status_code == 200 and "success" in response_data

    @allure.title('Получение ошибки при создании заказа неавторизованным пользователем')
    def test_make_an_order_no_auth_user(self):
        response = UserMethods.make_an_order_no_auth(ingredients)
        response_data = response.json()
        expected_response = {
            "success": False,
            "message": "You should be authorised"
        }
        assert response.status_code == 401 and response_data == expected_response

    @allure.title('Получение ошибки при создании заказа авторизованным пользователем без передачи ингридиентов')
    def test_make_an_order_auth_user_without_ingredients(self, generate_user_data):
        response_headers = generate_user_data['auth_headers']
        response = UserMethods.make_an_order_without_body(headers=response_headers)
        response_data = response.json()
        expected_response = {
            "success": False,
            "message": "Ingredient ids must be provided"
        }
        assert response.status_code == 400 and response_data == expected_response

    @allure.title('Успешное создание заказа авторизованного пользователя с передачей ингридиентов')
    def test_make_an_order_auth_user_with_incorrect_hash(self, generate_user_data):
        response_headers = generate_user_data['auth_headers']
        response = UserMethods.make_an_order(body=ingredients_2, headers=response_headers)
        html_code = response.text
        assert response.status_code == 500 and not "success" in html_code