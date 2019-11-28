from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('settings')

from home import views

db = SQLAlchemy(app)

from aluno import views