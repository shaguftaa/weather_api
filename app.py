
from flask import Flask
from api import *

app = Flask(__name__)

app.register_blueprint(forecast_api, url_prefix='/forecast')


@app.route("/health")
def health():
    return "Hello from Weather API!"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
