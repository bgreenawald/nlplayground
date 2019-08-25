import json
import requests

from flask import Blueprint, jsonify, render_template, request

api = Blueprint("api", __name__,)

API_KEY = "rZCF070Iie2PlGnpmXD2f7sa5Ys153Aj2x204KW9"

# Generic api
@api.route('/api/madgab', methods=["POST"])
def madgab():
    print(type(request.json))
    headers = {
        'Content-type': 'application/json',
        'x-api-key': API_KEY,
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'MadGab'
    url = '{}/{}'.format(base_url, resource_path)
    r = requests.post(url, data=json.dumps(request.json), headers=headers)
    print(r.json())
    return jsonify({"statusCode": r.status_code, "body": r.json()})

@api.route('/api/mixandmash', methods=["POST"])
def mix_and_mash():
    print(type(request.json))
    headers = {
        'Content-type': 'application/json',
        'x-api-key': API_KEY,
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'mix-and-mash'
    url = '{}/{}'.format(base_url, resource_path)
    r = requests.post(url, data=json.dumps(request.json), headers=headers)
    print(r.json())
    return jsonify({"statusCode": r.status_code, "body": r.json()})

@api.route('/api/nntextgen')
def nn_text_gen():


    headers = {
        'Content-type': 'application/json',
        'x-api-key': API_KEY,
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'nn-text-gen'
    url = '{}/{}'.format(base_url, resource_path)
    r = requests.post(url, data=json.dumps(request.json), headers=headers)

    return jsonify({"statusCode": r.status_code, "body": r.json()})
