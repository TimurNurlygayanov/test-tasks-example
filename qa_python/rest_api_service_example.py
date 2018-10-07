from uuid import uuid4
import flask
from flask import Flask
from flask import request
from flask_basicauth import BasicAuth


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'test_user'
app.config['BASIC_AUTH_PASSWORD'] = 'test_password'
basic_auth = BasicAuth(app)

BOOKS = []
SESSIONS = []


def verify_cookie(req):
    cookie = req.cookies.get('my_cookie', '')

    return bool(cookie in SESSIONS)


@app.route('/login', methods=['GET'])
@basic_auth.required
def get_auth():
    cookie = str(uuid4())
    SESSIONS.append(cookie)

    return flask.jsonify({'auth_cookie': cookie})


@app.route('/books', methods=['GET'])
def get_list_of_books():
    if verify_cookie(request):
        return flask.jsonify(BOOKS)


@app.route('/add_book', methods=['POST'])
def add_book():
    if verify_cookie(request):
        title = request.values.get('title', '')
        author = request.values.get('author', 'No Name')

        BOOKS.append({'title': title, 'author': author})



if __name__ == "__main__":
    app.run('0.0.0.0')
