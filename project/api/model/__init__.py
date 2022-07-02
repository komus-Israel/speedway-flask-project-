from sqlalchemy import UniqueConstraint
from ..services.extensions_services import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_admin.contrib.sqla import ModelView
from passlib.apps import custom_app_context as pwd_context

class Admins(db.Model):
    
    __tablename__ = "admins_table"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(200), index = True)
    last_name = db.Column(db.String(200), index =True)
    email = db.Column(db.String(200), index =True, unique=True)
    password_hash = db.Column(db.String(200), nullable = False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
    
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
        
    
class Students(db.Model):
    
    __tablename__ = "students"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(64), index = True)
    last_name = db.Column(db.String(64), index =True)
    email = db.Column(db.String(64), unique=True)
    department = db.Column(db.String(64), index=True)
    level = db.Column(db.String(64), index=True)
    matric_no = db.Column(db.String(64), index =True, unique=True)


class CustomModelView(ModelView):
    
    can_export = True
    can_delete = True 