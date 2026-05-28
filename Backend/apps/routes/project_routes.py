from flask import Blueprint
from flask_jwt_extended import jwt_required

from apps.controllers.project_controller import (
    create_project_handler,
    delete_project_handler,
    get_project_handler,
    list_projects_handler,
    update_project_handler,
)

project_bp = Blueprint("project", __name__)


@project_bp.route("/", methods=["GET"])
def list_projects():
    return list_projects_handler()


@project_bp.route("/", methods=["POST"])
@jwt_required()
def create_project():
    return create_project_handler()


@project_bp.route("/<int:project_id>", methods=["GET"])
def get_project(project_id):
    return get_project_handler(project_id)


@project_bp.route("/<int:project_id>", methods=["PUT"])
@jwt_required()
def update_project(project_id):
    return update_project_handler(project_id)


@project_bp.route("/<int:project_id>", methods=["DELETE"])
@jwt_required()
def delete_project(project_id):
    return delete_project_handler(project_id)
