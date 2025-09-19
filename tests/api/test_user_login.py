import allure
import pytest

from helpers.helpers import Helpers
from data.responses import Responses


@allure.suite('Логин пользователя')
class TestUserLogin:
    @allure.title('Успешный логин пользователя')
    def test_user_login_success(self, create_user_fx):
        user_data = Helpers.create_user_data()
        response = create_user_fx(user_data)
        assert response.status_code == 200

        response = Helpers.login_user(user_data)

        assert response.status_code == 200
        assert response.json()['success'] == True


    @pytest.mark.parametrize('field_name_error', ['email', 'password'])
    @allure.title('Неуспешный логин пользователя, если поле Логин некорректное')
    def test_user_wrong_login_error(self, create_user_fx, field_name_error):
        allure.dynamic.title(f'Неуспешный логин пользователя, если поле {field_name_error} некорректное')

        user_data = Helpers.create_user_data()
        response = create_user_fx(user_data)
        assert response.status_code == 200

        user_data[field_name_error] += 'fdf544sdfggfsdgdfs5ddf'
        response = Helpers.login_user(user_data)

        assert response.status_code == 401
        assert response.json() == Responses.USER_WRONG_LOGIN_PASSWORD_RESPONSE
