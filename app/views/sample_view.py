from flask import Blueprint, jsonify

bp = Blueprint("sample-view", __name__, url_prefix="/api")

@bp.route("/", methods=["GET"])
def hello_world():
    return jsonify({
        "message": "Hello, world!"
    })
