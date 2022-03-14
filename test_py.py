import os

from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)


@app.route("/")
def index():
    return """Это кто-нибудь прочитает??????
    Серъезно, кто вообще это читает
    Ваванчик привет"""


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
