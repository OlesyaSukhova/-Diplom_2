from faker import Faker

fake = Faker()

def generate_user_body():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

