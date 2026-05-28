from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize JWT
    JWTManager(app)

    # Routers
    from apps.routes.auth_routes import auth_bp
    from apps.routes.icon_routes import icon_bp
    from apps.routes.project_routes import project_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(icon_bp, url_prefix="/api/icons")
    app.register_blueprint(project_bp, url_prefix="/api/projects")

    return app