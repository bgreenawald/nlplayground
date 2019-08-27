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

@api.route('/api/nntextgen', methods=["POST"])
def nn_text_gen():

    headers = {
        'Content-type': 'application/json',
        'x-api-key': API_KEY,
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'nn-text-gen'
    url = '{}/{}'.format(base_url, resource_path)
    # r = requests.post(url, data=json.dumps(request.json), headers=headers)
    dummy_ret = [{"message": "brayd", "isOriginal": True, "sequence_matcher": "brayden", "levenshtein": "brayden", "damerau_levenshtein": "brady", "hamming": "brayden", "jaro": "brady", "jaro_winkler": "brady", "subsets": ["brayden", "braydon", "ray"]}, {"message": "denetrius", "isOriginal": True, "sequence_matcher": "demetrius", "levenshtein": "demetrius", "damerau_levenshtein": "demetrius", "hamming": "demetrius", "jaro": "demetrius", "jaro_winkler": "demetrius", "subsets": []}, {"message": "ben", "isOriginal": False}, {"message": "hrancisco", "isOriginal": True, "sequence_matcher": "francisco", "levenshtein": "francisco", "damerau_levenshtein": "francisco", "hamming": "francisco", "jaro": "francisco", "jaro_winkler": "francisco", "subsets": []}, {"message": "jacro", "isOriginal": True, "sequence_matcher": "jacob", "levenshtein": "jairo", "damerau_levenshtein": "jairo", "hamming": "jairo", "jaro": "jacob", "jaro_winkler": "jacob", "subsets": []}]
    return jsonify({"statusCode": 200, "body": dummy_ret})
