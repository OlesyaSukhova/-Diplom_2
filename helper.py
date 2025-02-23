from faker import Faker

fake = Faker()

def generate_user_body():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

class Url:
    base_url = "https://stellarburgers.nomoreparties.site/"
    create_user_url = "api/auth/register"
    login_user = "api/auth/login"
    user_info = "api/auth/user"
    make_an_order = "api/orders"
    receive_an_order = "api/orders"
