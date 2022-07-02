from flask import Blueprint, request, jsonify
from flask_restx import Resource, reqparse
from api.services.admin_services import ( 
    admin_registration_service, admin_login_service
)

from api.services.student_services import (
    admin_add_student_service, admin_fetch_student_by_id,
    admin_fetch_all_students, admin_update_student,
    admin_delete_student_resource
)
from api.services.extensions_services import admin, db, api
from api.model import Admins, CustomModelView, Students
from flask_jwt_extended import create_access_token, jwt_required
from flask_cors import  CORS, cross_origin
import json



parser = reqparse.RequestParser()
parser.add_argument('var1', type=str, help='variable 1')
parser.add_argument('var2', type=str, help='variable 2')

#   setup admin controller blueprint
adminController = Blueprint("admin", __name__)


#   setup CORS
CORS(adminController, resources={r"/admin*": {"origins":"*"}})

#   setup db in the admin view
admin.add_views(CustomModelView(Admins, db.session))
admin.add_views(CustomModelView(Students, db.session))

#   admin registration controller
@adminController.route("/register", methods= ["POST"])
def register_admin():
    
    #   return admin registration service
    return admin_registration_service(request.json)

#   admin login controller
@adminController.route("/login", methods= ["POST"])
def admin_login():
    
    #   return admin login service
    return admin_login_service(request.json)

#   admin controller to add new student data
@adminController.route("/students/new", methods= ["POST"])
@jwt_required()
def register_student():

    #   return admin service to add new students
    return admin_add_student_service(request.json)


#   controller to fetch students
@adminController.route("/students/get/<id>", methods= ["GET"])
@jwt_required()
def fetch_student_by_id(id):

    #   return the service to fetch students
    return admin_fetch_student_by_id(id)

#   controller to fetch all students
@adminController.route("/students/all/<int:page>", methods= ["GET"])
@jwt_required()
def fetch_all_students(page):
    
    #   return service that fetches all students
    return admin_fetch_all_students(page)

#   controller to update student resource
@adminController.route("/students/<uuid:id>/update", methods= ["PATCH"])
@jwt_required()
def update_student(id):

    #   return service to update the student resource
    return admin_update_student(id, request.json)

#   controller to delete students' data
@adminController.route("/students/delete/<uuid:id>", methods= ["DELETE"])
@jwt_required()
def delete_student(id):

    #   return the service to to delete the data
    return  admin_delete_student_resource(id)


        
