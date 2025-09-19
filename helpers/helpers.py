import allure
import requests
from faker import Faker

from data.urls import Urls


class Helpers:
    @allure.step('Создание фейкового пользователя')
    def create_user_data():
        faker = Faker()

        courier_data = {
            "email": faker.email(),
            "password": faker.password(),
            "name": faker.first_name()
        }

        return courier_data


    @allure.step('Отправка запроса на логин пользователя')
    def login_user(payload):
        url = Urls.LOGIN_USER_URL
        response = requests.post(url, json=payload)
        return response
    

    @allure.step('Отправка запроса на создание заказа без аутентификации')
    def create_order_no_token(payload):
        url = Urls.CREATE_ORDER_URL
        response = requests.post(url, json=payload)
        return response
    

    @allure.step('Отправка запроса на создание заказа с аутентификацией')
    def create_order(payload, token):
        url = Urls.CREATE_ORDER_URL
        headers = {
            "Authorization": f"{token}",
            "Content-Type": "application/json"
        }
            
        response = requests.post(url, json=payload, headers=headers)
        return response


    @allure.step('Отправка запроса на получение данных по ингредиенту')
    @staticmethod
    def get_ingredients_data():
        url = Urls.GET_INGREDIENTS_DATA_URL
        response = requests.get(url)
        return response
