from flask import jsonify, request
from app import app
from app.controllers import get_audio_sentiments_controller
from app.auth import api_key_required

# Map route to controller function with API key authentication
@app.route("/get_audio_sentiments", methods=["GET"])
@api_key_required
def get_audio_sentiments_route():
    return get_audio_sentiments_controller()
