from flask import Flask, Blueprint
from routes import *
from db import  Base, engine
from flask_cors import CORS

app=Flask(__name__)

[
    app.register_blueprint(route)
    for route in globals().values()
    if isinstance(route, Blueprint)
]

CORS(app)
with app.app_context():
    Base.metadata.create_all(engine)

@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'