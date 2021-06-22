from flask import Flask
import os
import urllib
import redis


target = os.getenv("target")
REDIS_URL = os.getenv("REDIS_URL")

app = Flask(__name__)

app.redis_storage = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)


@app.route("/")
def index():
    with urllib.request.urlopen(target) as response:
        html = response.read()
    return html


@app.route("/redis/get/<something>")
def redis_get(something):
    result = app.redis_storage.get(something)
    if not result:
        result = "nope"
    return result


@app.route("/redis/set/<something>")
def redis_set(something):
    app.redis_storage.set(something, 'bingo', 900)
    return something


if __name__ == "__main__":
    app.run()
