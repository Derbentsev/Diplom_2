import allure
import pytest

from helpers.helpers import Helpers
from data.responses import Responses


@allure.suite('Создание пользователя')
class TestCreateUser:
    @allure.title('Успешное создание пользователя')
    def test_create_user_success(self, create_user_fx):
        user_data = Helpers.create_user_data()
        response = create_user_fx(user_data)

        assert response.status_code == 200
        assert response.json()['success'] == True


    @allure.title('Неуспешное создание пользователя, если такой пользователь уже существует')
    def test_create_user_already_exists_error(self, create_user_fx):
        user_data = Helpers.create_user_data()
        response = create_user_fx(user_data)

        assert response.status_code == 200
    
        response = create_user_fx(user_data)

        assert response.status_code == 403        
        assert response.json() == Responses.USER_ALREADY_EXISTS_RESPONSE


    @pytest.mark.parametrize('field_to_remove', ['email', 'password', 'name'])
    def test_create_user_missing_field_error(self, create_user_fx, field_to_remove):
        allure.dynamic.title(f'Неуспешное создание пользователя, если не указан {field_to_remove}')

        user_data = Helpers.create_user_data()
        del user_data[field_to_remove]
        response = create_user_fx(user_data)

        assert response.status_code == 403        
        assert response.json() == Responses.USER_NOT_EXISTS_FIELD_RESPONSE
