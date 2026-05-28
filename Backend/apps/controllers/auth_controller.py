import logging

from flask import request
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

from apps.services.auth_service import validate_credentials
from apps.utils.response import error_response, success_response

logger = logging.getLogger(__name__)


def login_handler():
    data = request.get_json() or {}
    try:
        username = data.get("username")
        password = data.get("password")
        if not username or not password:
            return error_response("Username and password are required.", status=422)

        if not validate_credentials(username, password):
            return error_response("Invalid credentials.", status=401)

        token = create_access_token(identity=username)
        return success_response({"access_token": token})
    except ValidationError as exc:
        return error_response("Validation error.", status=422, errors=exc.messages)
    except Exception:
        logger.exception("Unexpected error during login.")
        return error_response("Internal server error.", status=500)
