import allure

from data.data import Data
from helpers.helpers import Helpers
from data.responses import Responses


@allure.suite('Создание заказа')
class TestCreateOrder:
    @allure.title('Создание заказа с аутентификацией')
    def test_create_order_with_auth_success(self, create_user_fx):
        user_data = Helpers.create_user_data()
        response = create_user_fx(user_data)
        assert response.status_code == 200

        token = response.json()['accessToken']
    
        ingredients_ids = Data.INGREDIENTS_IDS
        response = Helpers.create_order(ingredients_ids, token)

        assert response.status_code == 200
        assert response.json()['success'] == True


    @allure.title('Неуспешное создание заказа без аутентификации')
    def test_create_order_without_auth_error(self):
        ingredients_ids = Data.INGREDIENTS_IDS
        response = Helpers.create_order_no_token(ingredients_ids)

        assert response.status_code == 401
        assert response.json()['success'] == False


    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_user_fx):
        user_data = Helpers.create_user_data()
        response = create_user_fx(user_data)
        assert response.status_code == 200

        token = response.json()['accessToken']
    
        ingredients_ids = {"ingredients": []}
        response = Helpers.create_order(ingredients_ids, token)

        assert response.status_code == 400
        assert response.json() == Responses.CREATE_ORDER_NO_INGREDIENTS_RESPONSE



    @allure.title('Создание заказа с некоррекными ингредиентами')
    def test_create_order_with_wrong_id_ingredients(self, create_user_fx):
        user_data = Helpers.create_user_data()
        response = create_user_fx(user_data)
        assert response.status_code == 200

        token = response.json()['accessToken']
    
        ingredients_ids = {"ingredients": ['fdfs44']}
        response = Helpers.create_order(ingredients_ids, token)

        assert response.status_code == 400
