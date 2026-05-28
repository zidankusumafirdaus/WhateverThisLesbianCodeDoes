import logging
from pathlib import Path

from flask import Response, send_from_directory

from apps.schemas.icon_schema import IconResponseSchema
from apps.services.icon_service import get_icon, list_icons
from apps.utils.db import get_db_session
from apps.utils.response import error_response, success_response

logger = logging.getLogger(__name__)


def _get_icons_dir():
    # Backend/apps/controllers/icon_controller.py -> Backend/apps/icons/
    return Path(__file__).resolve().parents[1] / "icons"


def list_icons_handler():
    try:
        with get_db_session() as db:
            data = list_icons(db)
            return success_response(IconResponseSchema(many=True).dump(data))
    except Exception:
        logger.exception("Unexpected error while listing icons.")
        return error_response("Internal server error.", status=500)


def get_icon_handler(icon_id):
    try:
        with get_db_session() as db:
            icon = get_icon(db, icon_id)
            if not icon:
                return error_response("Icon not found.", status=404)
            return success_response(IconResponseSchema().dump(icon))
    except Exception:
        logger.exception("Unexpected error while fetching icon.")
        return error_response("Internal server error.", status=500)


def get_icon_display_handler(filename):
    # Serve static icon assets from Backend/apps/icons/**
    icons_dir = _get_icons_dir()
    return send_from_directory(str(icons_dir), filename, as_attachment=False)
