from flask import Flask
import logging
import os

app = Flask(__name__)
logger = logging.getLogger('app')
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)7s | %(name)26s | %(funcName)s: %(message)s"
)
logger.setLevel(logging.DEBUG)


@app.route("/")
def hello():
    logger.info('Логгер INFO')
    logger.warning('Ещё один логгер')
    return "Flask inside Docker!!"


if __name__ == "__main__":
    port = 3478
    app.run(debug=True,host='0.0.0.0',port=port)
