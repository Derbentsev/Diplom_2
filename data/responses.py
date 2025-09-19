class Responses:
    USER_ALREADY_EXISTS_RESPONSE = {
        "success": False,
        "message": "User already exists"
    }

    USER_NOT_EXISTS_FIELD_RESPONSE = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    USER_WRONG_LOGIN_PASSWORD_RESPONSE = {
        "success": False,
        "message": "email or password are incorrect"
    }

    CREATE_ORDER_NO_INGREDIENTS_RESPONSE = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }
