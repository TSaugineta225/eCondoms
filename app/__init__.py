from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from authlib.integrations.flask_client import OAuth
import json
import os, sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tenerife225sauginhalicale'
app.config['DATABASE'] = 'usuarios.db'


from app.views import index