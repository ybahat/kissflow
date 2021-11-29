from flask import Flask, jsonify, request

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    params = request.get_json()
    return jsonify(params)


if __name__ == '__main__':
    my_awesome_app.run()