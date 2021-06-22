from flask import Flask
import os
import urllib

app = Flask(__name__)

target = os.getenv("target")


@app.route("/")
def index():
    with urllib.request.urlopen(target) as response:
        html = response.read()
    return html


if __name__ == "__main__":
    app.run()
