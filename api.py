"""The AWS Lambda calls for the application."""

import json
from typing import Any, Dict

import aiohttp
import async_timeout
from quart import Blueprint, jsonify, request, Response

api = Blueprint("api", __name__,)

BASE_URL = "https://e5atpy4c73.execute-api.us-east-1.amazonaws.com/Prod"

# Generic api
@api.route("/api/madgab", methods=["POST"])
async def madgab() -> Response:
    """
    Call the Madgab Lambda function.

    Returns:
        Response: The response from the Lambda function.
    """
    API_KEY = "ZHLM6JdUyQaP1P2cpG1g54IhGk6Xf6Cv9vnIOLmL"
    HEADERS = {
        "Content-type": "application/json",
        "x-api-key": API_KEY,
    }
    resource_path = "MadGab"
    url = "{}/{}".format(BASE_URL, resource_path)
    data = await request.json
    async with aiohttp.ClientSession() as session, async_timeout.timeout(30):
        async with session.post(
            url, headers=HEADERS, data=json.dumps(data)
        ) as response:
            body = await response.json()
            status_code = response.status
    return jsonify({"statusCode": status_code, "body": body})


@api.route("/api/mixandmash", methods=["POST"])
async def mix_and_mash() -> Response:
    """
    Call the Mix and Mash Lambda function.

    Returns:
        Response: The response from the Lambda function..
    """
    API_KEY = "rZCF070Iie2PlGnpmXD2f7sa5Ys153Aj2x204KW9"
    HEADERS = {
        "Content-type": "application/json",
        "x-api-key": API_KEY,
    }
    resource_path = "mix-and-mash"
    url = "{}/{}".format(BASE_URL, resource_path)
    data = await request.json
    async with aiohttp.ClientSession() as session, async_timeout.timeout(30):
        async with session.post(
            url, headers=HEADERS, data=json.dumps(data)
        ) as response:
            body = await response.json()
            status_code = response.status
    return jsonify({"statusCode": status_code, "body": body})


@api.route("/api/nntextgen", methods=["POST"])
async def nn_text_gen() -> Response:
    """
    Call the NN Text Gen Lambda function.

    Returns:
        Response: The response from the Lambda function.
    """
    api_map = {
        "boy_names": "ixczTTsgoAhhBxnlu81Z7Z9X3KdXVXw4xjBh3j1a",
        "girl_names": "z1mqdfws2q6LeXu3jb42E1dG2eEaaNW41ZwgUpUX",
        "pokemon_names": "VtHCLH7esP3puWP8dluVZ8MaPWD4pjdP79ozmni0",
        "dinosaur_names": "ftvixoys3B8TmBey6fwsp2qdJDd9C0Vq8X9f3iOB",
        "stripper_names": "UCYMsD6ZSt5HWpRDbECJiSAKaqbaPQ43ucWIgYU1",
    }

    data = await request.json

    try:
        API_KEY = api_map[data["project"]]
        HEADERS = {
            "Content-type": "application/json",
            "x-api-key": API_KEY,
        }
    except KeyError as e:
        return jsonify({"statusCode": 400, "body": str(e)})

    try:
        payload = validate(data)
    except Exception as e:
        return jsonify({"statusCode": 400, "body": str(e)})

    resource_path = "nn_" + data["project"]
    url = "{}/{}".format(BASE_URL, resource_path)
    async with aiohttp.ClientSession() as session, async_timeout.timeout(30):
        async with session.post(
            url, headers=HEADERS, data=json.dumps(payload)
        ) as response:
            body = await response.json()
            status_code = response.status
    return jsonify({"statusCode": status_code, "body": body})


def validate(body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate the types of the request payload.

    Args:
        body (Dict[str, Any]): Request data.

    Returns:
        Dict[str, Any]: Request data after type validation and transformation.
    """
    body["seed"] = str(body.get("seed", ""))
    body["iters"] = int(body.get("iters", 5))
    body["exact"] = bool(body.get("exact", True))
    body["temperature"] = float(body.get("temperature", 1.0))
    body["same_start"] = bool(body.get("same_start", True))
    body["postprocess"] = bool(body.get("postprocess", False))
    return body
