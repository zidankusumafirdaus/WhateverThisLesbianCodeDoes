from flask import Blueprint

from apps.controllers.auth_controller import login_handler

auth_bp = Blueprint("auth", __name__)


auth_bp.route("/login", methods=["POST"])(login_handler)
