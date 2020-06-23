from app import app
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
import os

app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import StockSet