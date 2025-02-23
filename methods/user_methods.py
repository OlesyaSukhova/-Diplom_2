import requests

from helper import Url


class UserMethods:
    @staticmethod
    def create_user(body):
        return requests.post(f'{Url.base_url}{Url.create_user_url}', json=body)

    @staticmethod
    def login_user(body):
        return requests.post(f'{Url.base_url}{Url.login_user}', json=body)

    @staticmethod
    def change_user_info(body, headers):
        return requests.patch(f'{Url.base_url}{Url.user_info}', json=body, headers=headers)

    @staticmethod
    def change_user_info_without_auth(body):
        return requests.patch(f'{Url.base_url}{Url.user_info}', json=body)

    @staticmethod
    def make_an_order(body, headers):
        return requests.post(f'{Url.base_url}{Url.make_an_order}', json=body, headers=headers)

    @staticmethod
    def make_an_order_no_auth(body):
        return requests.post(f'{Url.base_url}{Url.make_an_order}', json=body)

    @staticmethod
    def make_an_order_without_body(headers):
        return requests.post(f'{Url.base_url}{Url.make_an_order}', headers=headers)

    @staticmethod
    def receive_an_order(headers):
        return requests.get(f'{Url.base_url}{Url.receive_an_order}', headers=headers)

    @staticmethod
    def receive_an_order_no_auth_user():
        return requests.get(f'{Url.base_url}{Url.receive_an_order}')



