import random
import string

class DataGenerator:
    @staticmethod
    def generate_registration_data():
        name = "Дарья Алексеева"
        random_num = random.randint(100, 999)
        email = f"darya_alekseeva_39_{random_num}@yandex.ru"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return name, email, password
    
    @staticmethod
    def generate_short_password():
        return ''.join(random.choices(string.ascii_letters, k=5))
    
    @staticmethod
    def generate_email():
        random_num = random.randint(100,999)
        return f"test_{random_num}@mail.ru"
    
    @staticmethod
    def generate_name():
        names = ["Дарья Алексеева", "Сатору Годжи", "Борис Животное"]
        return random.choice(names)