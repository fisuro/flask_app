from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://axnbpeci:rADWtHAG9X0UDVyrJyvenm8-uX4GjZmR@tyke.db.elephantsql.com/axnbpeci'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from core import views