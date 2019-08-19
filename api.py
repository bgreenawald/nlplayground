import json
import requests

from flask import Blueprint, jsonify, render_template, request

api = Blueprint("api", __name__,)

# Generic api
@api.route('/api/madgab', methods=["POST"])
def madgab():
    print(type(request.json))
    headers = {
        'Content-type': 'application/json',
        'x-api-key': 'ZHLM6JdUyQaP1P2cpG1g54IhGk6Xf6Cv9vnIOLmL',
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'MadGab'
    url = '{}/{}'.format(base_url, resource_path)
    r = requests.post(url, data=json.dumps(request.json), headers=headers)
    print(r.json())
    return jsonify({"status_code": r.status_code, "message": r.json()})

@api.route('/api/mixandmash', methods=["POST"])
def mixandmash():
    print(type(request.json))
    headers = {
        'Content-type': 'application/json',
        'x-api-key': 'rZCF070Iie2PlGnpmXD2f7sa5Ys153Aj2x204KW9',
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'mix-and-mash'
    url = '{}/{}'.format(base_url, resource_path)
    r = requests.post(url, data=json.dumps(request.json), headers=headers)
    print(r.json())
    return jsonify({"status_code": r.status_code, "message": r.json()})
