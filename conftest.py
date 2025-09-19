import allure
import pytest
import requests

from data.urls import Urls


@pytest.fixture
@allure.step('Отправка запроса на создание пользователя')
def create_user_fx():
    def create_user(user_data):
        url = Urls.CREATE_USER_URL
        response = requests.post(url, json=user_data)
        return response
    
    return create_user
