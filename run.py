from flask import Flask, jsonify, request
import requests
import json

planner_patch_app = Flask(__name__)


@planner_patch_app.route('/', methods=['POST'])
def hello_world_post():
    params = request.get_json()

    # headers = {
    #     "Authorization": params["AuthorizationToken"],
    #     "If-Match": params["IfMatch"]
    #
    # }
    #
    # url = "https://graph.microsoft.com/v1.0/planner/tasks/" + params["TaskId"] + "/details"
    #
    # payload = {
    #     "description" : params["description"]
    # }

    # r = requests.post(url, data=json.dumps(payload), headers=headers)
    return request.data


@planner_patch_app.route('/', methods=['GET'])
def hello_world_get():
    return 'Hello World!'


if __name__ == '__main__':
    planner_patch_app.run()