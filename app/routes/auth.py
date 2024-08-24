from flask import Blueprint, request, jsonify
import jwt
import datetime
from app.utils.jwt_helper import encode_jwt_token

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if auth and auth.username == 'user' and auth.password == 'password':
        token = encode_jwt_token(auth.username)
        return jsonify({'token': token})

    return jsonify({'message': 'Could not verify!'}), 401
