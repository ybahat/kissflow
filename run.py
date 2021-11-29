from flask import Flask, jsonify, request

planner_patch_app = Flask(__name__)


@planner_patch_app.route('/', methods=['POST'])
def hello_world():
    params = request.get_json()
    return jsonify(params)


@planner_patch_app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    planner_patch_app.run()