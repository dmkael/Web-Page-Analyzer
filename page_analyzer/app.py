from flask import Flask
import os
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def hello():
    return f"Hello, world {os.getenv('SECRET_KEY')}"
