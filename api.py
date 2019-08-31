import json

import aiohttp
import asyncio
import async_timeout
import requests
from quart import Blueprint, jsonify, render_template, request

api = Blueprint("api", __name__,)

API_KEY = "rZCF070Iie2PlGnpmXD2f7sa5Ys153Aj2x204KW9"


# Generic api
@api.route('/api/madgab', methods=["POST"])
async def madgab():
    headers = {
        'Content-type': 'application/json',
        'x-api-key': API_KEY,
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'MadGab'
    data = await request.json
    url = '{}/{}'.format(base_url, resource_path)
    async with aiohttp.ClientSession() as session, async_timeout.timeout(30):
        async with session.post(url, headers=headers, data=json.dumps(data)) as response:
            body = await response.json()
            status_code = response.status
    return jsonify({"statusCode": status_code, "body": body})


@api.route('/api/mixandmash', methods=["POST"])
async def mix_and_mash():
    headers = {
        'Content-type': 'application/json',
        'x-api-key': API_KEY,
    }

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'mix-and-mash'
    url = '{}/{}'.format(base_url, resource_path)
    data = await request.json
    url = '{}/{}'.format(base_url, resource_path)
    async with aiohttp.ClientSession() as session, async_timeout.timeout(30):
        async with session.post(url, headers=headers, data=json.dumps(data)) as response:
            body = await response.json()
            status_code = response.status
    return jsonify({"statusCode": status_code, "body": body})


@api.route('/api/nntextgen', methods=["POST"])
async def nn_text_gen():
    headers = {
        'Content-type': 'application/json',
        'x-api-key': API_KEY,
    }

    data = await request.json
    try:
        payload = validate(data)
    except Exception as e:
        return jsonify({"statusCode": 400, "body": str(e)})

    base_url = 'https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod'
    resource_path = 'nn-text-gen'
    url = '{}/{}'.format(base_url, resource_path)
    async with aiohttp.ClientSession() as session, async_timeout.timeout(30):
        async with session.post(url, headers=headers, data=json.dumps(payload)) as response:
            body = await response.json()
            status_code = response.status
    return jsonify({"statusCode": status_code, "body": body})


def validate(body):
    body["seed"] = str(body.get("seed", ""))
    body["iters"] = int(body.get("iters", 5))
    body["exact"] = bool(body.get("exact", True))
    body["temperature"] = float(body.get("temperature", 1.0))
    body["same_start"] = bool(body.get("same_start", True))
    body["postprocess"] = bool(body.get("postprocess", False))
    return body
