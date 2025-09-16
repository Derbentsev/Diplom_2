import allure

from data.data import Data
from helpers.helpers import Helpers
from data.responses import Responses


@allure.suite('Создание пользователя')
class TestCreateUser:
    @allure.title('Успешное создание пользователя')
    def test_create_user_success(self):
        user_data = Helpers.create_user_data()
        response = Helpers.create_user(user_data)

        assert response.status_code == 200
        assert response.json()['success'] == True


    @allure.title('Неуспешное создание пользователя, если такой пользователь уже существует')
    def test_create_user_already_exists_error(self):
        user_data = Data.USER_ALREADY_EXISTS_DATA
        response = Helpers.create_user(user_data)

        assert response.status_code == 403        
        assert response.json() == Responses.USER_ALREADY_EXISTS_RESPONSE


    @allure.title('Неуспешное создание пользователя, если не указан email')
    def test_create_user_no_field_email_error(self):
        user_data = Helpers.create_user_data()
        del user_data['email']
        response = Helpers.create_user(user_data)

        assert response.status_code == 403        
        assert response.json() == Responses.USER_NOT_EXISTS_FIELD_RESPONSE


    @allure.title('Неуспешное создание пользователя, если не указан пароль')
    def test_create_user_no_field_password_error(self):
        user_data = Helpers.create_user_data()
        del user_data['password']
        response = Helpers.create_user(user_data)

        assert response.status_code == 403        
        assert response.json() == Responses.USER_NOT_EXISTS_FIELD_RESPONSE


    @allure.title('Неуспешное создание пользователя, если  не указано имя')
    def test_create_user_no_field_name_error(self):
        user_data = Helpers.create_user_data()
        del user_data['name']
        response = Helpers.create_user(user_data)

        assert response.status_code == 403        
        assert response.json() == Responses.USER_NOT_EXISTS_FIELD_RESPONSE
