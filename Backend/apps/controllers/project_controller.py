import logging
import time

from flask import request
from marshmallow import ValidationError
from sqlalchemy.exc import OperationalError

from apps.schemas.project_schema import (
    ProjectCreateSchema,
    ProjectResponseSchema,
    ProjectUpdateSchema,
)
from apps.services.project_service import (
    create_project,
    delete_project,
    get_project,
    list_projects,
    update_project,
)
from apps.utils.db import get_db_session
from apps.utils.response import error_response, success_response

logger = logging.getLogger(__name__)


def _is_deadlock_error(exc):
    original = getattr(exc, "orig", None)
    if not original or not getattr(original, "args", None):
        return False
    return original.args[0] == 1213


def _with_deadlock_retry(action, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return action()
        except OperationalError as exc:
            if _is_deadlock_error(exc) and attempt < max_attempts - 1:
                time.sleep(0.2 * (attempt + 1))
                continue
            raise


def list_projects_handler():
    page = request.args.get("page", default=1, type=int)
    page_size = request.args.get("page_size", default=10, type=int)
    status = request.args.get("status")
    location = request.args.get("location")
    title = request.args.get("title")
    search = request.args.get("search")

    with get_db_session() as db:
        result = list_projects(
            db,
            page=page,
            page_size=page_size,
            status=status,
            location=location,
            title=title,
            search=search,
        )
        payload = {
            "items": ProjectResponseSchema(many=True).dump(result["items"]),
            "pagination": result["pagination"],
        }
        return success_response(payload)


def get_project_handler(project_id):
    with get_db_session() as db:
        project = get_project(db, project_id)
        if not project:
            return error_response("Project not found.", status=404)
        return success_response(ProjectResponseSchema().dump(project))


def create_project_handler():
    data = request.get_json() or {}
    try:
        payload = ProjectCreateSchema().load(data)
        def _run():
            with get_db_session() as db:
                project = create_project(db, payload)
                return success_response(
                    ProjectResponseSchema().dump(project), status=201
                )

        return _with_deadlock_retry(_run)
    except ValidationError as exc:
        return error_response("Validation error.", status=422, errors=exc.messages)
    except Exception as exc:
        logger.exception("Unexpected error while creating project.")
        return error_response("Internal server error.", status=500)


def update_project_handler(project_id):
    data = request.get_json() or {}
    try:
        payload = ProjectUpdateSchema().load(data, partial=True)
        def _run():
            with get_db_session() as db:
                project = update_project(db, project_id, payload)
                if not project:
                    return error_response("Project not found.", status=404)
                return success_response(ProjectResponseSchema().dump(project))

        return _with_deadlock_retry(_run)
    except ValidationError as exc:
        return error_response("Validation error.", status=422, errors=exc.messages)
    except Exception as exc:
        logger.exception("Unexpected error while updating project.")
        return error_response("Internal server error.", status=500)


def delete_project_handler(project_id):
    with get_db_session() as db:
        deleted = delete_project(db, project_id)
        if not deleted:
            return error_response("Project not found.", status=404)
        return success_response(message="Project deleted.")
