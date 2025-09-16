import allure

from data.data import Data
from helpers.helpers import Helpers
from data.responses import Responses


@allure.suite('Логин пользователя')
class TestUserLogin:
    @allure.title('Успешный логин пользователя')
    def test_user_login_success(self):
        user_data = Data.USER_ALREADY_EXISTS_DATA
        response = Helpers.login_user(user_data)

        assert response.status_code == 200
        assert response.json()['success'] == True


    @allure.title('Неуспешный логин пользователя, если поле Логин некорректное')
    def test_user_wrong_login_error(self):
        user_data = Data.USER_ALREADY_EXISTS_DATA
        user_data['email'] += 'fdf544sdfggfsdgdfs5ddf'
        response = Helpers.login_user(user_data)

        assert response.status_code == 401
        assert response.json() == Responses.USER_WRONG_LOGIN_PASSWORD_RESPONSE


    @allure.title('Неуспешный логин пользователя, если поле Пароль некорректное')
    def test_user_wrong_password_error(self):
        user_data = Data.USER_ALREADY_EXISTS_DATA
        user_data['password'] += 'fdf5445ddf'
        response = Helpers.login_user(user_data)

        assert response.status_code == 401
        assert response.json() == Responses.USER_WRONG_LOGIN_PASSWORD_RESPONSE
