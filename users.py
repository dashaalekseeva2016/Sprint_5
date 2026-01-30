from generators import DataGenerator
import random

class Credentials:
        name = "Дарья Алексеева",
        email = "AlekseevaD_39@mail.ru",
        password = "123456"

class TestUsers:
    @staticmethod
    def get_valid_users():
        name, email, password = DataGenerator.generate_registration_data()
        return {
            "name": name,
            "email": email,
            "password": password
        }
    @staticmethod
    def get_user_with_short_password():  
        return {
            "name": "Дарья Алексеева",
            "email": "darya@example.com",
            "password": "123"  
        }
        
    FIXED_SHORT_PASSWORD_USERS = {
        "name": "Дарья Алексеева",
        "email": "darya_alekseeva_39_456@yandex.ru",
        "password": "123"
    }