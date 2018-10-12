import flask


app = flask.Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, world"


if __name__ == "__main__":
    app.run('0.0.0.0', port=7000)
