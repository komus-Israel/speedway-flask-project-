from flask_migrate import Migrate
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Resource, Api

migrate = Migrate()
db = SQLAlchemy()
jwt = JWTManager()
api = Api(version="1.0", title="Student Management API", description="Student Management MVC API", doc="/doc")

admin = Admin(name=None, template_mode="bootstrap4", url="/master", endpoint="master")