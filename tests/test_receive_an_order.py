import allure

from data import ingredients
from methods.user_methods import UserMethods


class TestReceiveAnOrder:
    @allure.title('Успешное получение списка заказов авторизованного пользователя')
    def test_order_list_auth_user(self, generate_user_data):
        response_headers = generate_user_data['auth_headers']
        response = UserMethods.make_an_order(body=ingredients, headers=response_headers)
        response_second = UserMethods.receive_an_order(response_headers)
        response_second_data = response.json()
        assert response_second.status_code == 200 and "success" in response_second_data

    @allure.title('Получение ошибки при запросе списка заказов неавторизованного пользователя')
    def test_order_list(self):
        response = UserMethods.receive_an_order_no_auth_user()
        response_data = response.json()
        expected_response = {
            "success": False,
            "message": "You should be authorised"
        }
        assert response.status_code == 401 and response_data == expected_response
