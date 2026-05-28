from flask import Blueprint

from apps.controllers.icon_controller import (
    get_icon_display_handler,
    get_icon_handler,
    list_icons_handler,
)

icon_bp = Blueprint("icon", __name__)


@icon_bp.route("/", methods=["GET"])
def list_icons():
    return list_icons_handler()


@icon_bp.route("/<int:icon_id>", methods=["GET"])
def get_icon(icon_id):
    return get_icon_handler(icon_id)


@icon_bp.route("/display/<path:filename>", methods=["GET"])
def get_icon_display(filename):
    return get_icon_display_handler(filename)
