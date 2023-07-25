from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'eb919f4762ee39353d69e70d67d3b6edf3f651493a0709e6028655a1c94c23f4'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather_app.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "631b88c88ba91ec86b342e957271d201"

from weather import routes
