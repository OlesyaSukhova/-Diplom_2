import allure
import requests

from curl import Url


class UserMethods:
    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(body):
        return requests.post(f'{Url.base_url}{Url.create_user_url}', json=body)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(body):
        return requests.post(f'{Url.base_url}{Url.login_user}', json=body)

    @staticmethod
    @allure.step('Изменение информации авторизованного пользователя')
    def change_user_info(body, headers):
        return requests.patch(f'{Url.base_url}{Url.user_info}', json=body, headers=headers)

    @staticmethod
    @allure.step('Изменение информации не авторизованного пользователя')
    def change_user_info_without_auth(body):
        return requests.patch(f'{Url.base_url}{Url.user_info}', json=body)

    @staticmethod
    @allure.step('Создание заказа авторизованным пользователем')
    def make_an_order(body, headers):
        return requests.post(f'{Url.base_url}{Url.make_an_order}', json=body, headers=headers)

    @staticmethod
    @allure.step('Создание заказа не авторизованным пользователем')
    def make_an_order_no_auth(body):
        return requests.post(f'{Url.base_url}{Url.make_an_order}', json=body)

    @staticmethod
    @allure.step('Попытка создать заказ без передачи тела запроса')
    def make_an_order_without_body(headers):
        return requests.post(f'{Url.base_url}{Url.make_an_order}', headers=headers)

    @staticmethod
    @allure.step('Получение списка заказов')
    def receive_an_order(headers):
        return requests.get(f'{Url.base_url}{Url.receive_an_order}', headers=headers)

    @staticmethod
    @allure.step('Получение списка заказов не авторизованным пользователем')
    def receive_an_order_no_auth_user():
        return requests.get(f'{Url.base_url}{Url.receive_an_order}')

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(headers):
        return requests.delete(f'{Url.base_url}{Url.user_info}', headers=headers)





