from flask import request, jsonify

def authenticate_api_key(api_key):
    if "API-Key" not in request.headers:
        return False
    return request.headers["API-Key"] == api_key

def api_key_required(func):
    def wrapper(*args, **kwargs):
        api_key = "sentimentanalysis"
        if not authenticate_api_key(api_key):
            return jsonify({"error": "Invalid API key"}), 401
        return func(*args, **kwargs)
    return wrapper
