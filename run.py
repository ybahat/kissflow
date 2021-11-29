from flask import Flask, jsonify, request

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/', methods=['POST'])
def hello_world():
    params = request.get_json()
    return jsonify(params)


@my_awesome_app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    my_awesome_app.run()