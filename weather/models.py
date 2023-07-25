import requests
from weather import BASE_URL, API_KEY, db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    country = db.Column(db.String(length=100), nullable=False)
    city = db.Column(db.String(length=100), nullable=False)

    @property  # adding a property named password to class User
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class WeatherInfo:
    def __init__(self, city):
        self.city = city
        url = BASE_URL + "appid=" + API_KEY + "&q=" + self.city
        response = requests.get(url).json()
        self.temp = response['main']['temp']
        self.humidity = response['main']['humidity']
        self.description = response['weather'][0]['description']
        self.wind_speed = response['wind']['speed']

    def kelvin_to_celsius(self):
        return round((self.temp - 273.15), 2)

    def kelvin_to_fahrenheit(self):
        return round(((self.temp - 273.15) * 1.8 + 32), 2)
