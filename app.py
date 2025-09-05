import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


#Ruta principal home
@app.route('/')
def index():
    return 'Hola mundo'