import http
from flask import request
from api.services.admin_services import admin_registration_service
from api.services.extensions_services import api
from flask_restx import  Resource, fields

namespace = api.namespace('', 'Admin related endpoints')

'''
    models
'''

admin_registration_model = api.model("admin_registration", {
    
    "first_name" : fields.String(readonly=True, description = "admin first name"),
    "last_name" : fields.String(readonly=True, description = "admin last name"),
    "email" : fields.String(readonly=True, description = "admin email"),
    "password" : fields.String(readonly=True, description = "admin password")
})

admin_login_model = api.model("admin_login", {
    
    "email" : fields.String(readonly=True, description = "admin email"),
    "password" : fields.String(readonly=True, description = "admin password")

})


student_registration_model = api.model("student_registration", {
    
    "first_name" : fields.String(readonly=True, description = "student first name"),
    "last_name" : fields.String(readonly=True, description = "student last name"),
    "email" : fields.String(readonly=True, description = "student email"),
    "matric_no" : fields.String(readonly=True, description = "student matric no"),
    "department" : fields.String(readonly=True, description = "student department"),
    "level" : fields.String(readonly=True, description = "student level"),
    
})


student_model = api.model("student_registration", {
    
    "id" : fields.String(readonly=True, description = "student id"),
    "first_name" : fields.String(readonly=True, description = "student first name"),
    "last_name" : fields.String(readonly=True, description = "student last name"),
    "email" : fields.String(readonly=True, description = "student email"),
    "matric_no" : fields.String(readonly=True, description = "student matric no"),
    "department" : fields.String(readonly=True, description = "student department"),
    "level" : fields.String(readonly=True, description = "student level"),
    
})



@namespace.response(http.HTTPStatus.CREATED, 'admin registered successfully')
@namespace.response(http.HTTPStatus.FORBIDDEN, 'admin credentials exists already')
@namespace.response(http.HTTPStatus.BAD_REQUEST, '{field_name} is missing in your request')
@namespace.route("/register")
class RegisterAdmin(Resource):

    @namespace.expect(admin_registration_model, 201)
    @namespace.doc("admin registration")

    def post(self):
        '''
            Register the admin 
        '''

        return self


@namespace.response(http.HTTPStatus.ACCEPTED, 'logged in successfully')
@namespace.response(http.HTTPStatus.NOT_FOUND, 'invalid credentials')
@namespace.response(http.HTTPStatus.BAD_REQUEST, '{field_name} is missing in your request')
@namespace.route("/login")
class AdminLogin(Resource):
    
    @namespace.expect(admin_login_model, 201)
    @namespace.doc("admin login")

    def post(self):
        '''
            admin login
        '''
        return self



@namespace.response(http.HTTPStatus.CREATED, 'student registered successfully')
@namespace.response(http.HTTPStatus.FORBIDDEN, 'existing email')
@namespace.response(http.HTTPStatus.FORBIDDEN, 'existing matric')
@namespace.response(http.HTTPStatus.BAD_REQUEST, '{field_name} is missing in your request')
@namespace.route("/students/new")
class RegisterStudent(Resource):
    
    @namespace.expect(student_registration_model, 201)
    @namespace.doc("register new student")

    def post(self):
        '''
            new student
        '''
        return self 



@namespace.response(http.HTTPStatus.FORBIDDEN, 'invalid id type')
@namespace.response(http.HTTPStatus.NOT_FOUND, 'invalid id')
@namespace.route("/students/get/<uuid:id>")
@namespace.param('id', 'The student')
class FetchStudentById(Resource):
    
    
    @namespace.marshal_with(student_model)
    @namespace.doc("fetch student by id")

    def get(self):
        '''
            fetch student by id
        '''
        return self 


@namespace.route("/students/all/<int:page>")
@namespace.param('page', 'The page number')
class FetchStudentById(Resource):
    
    
    @namespace.marshal_list_with(student_model)
    @namespace.doc("fetch all students by page")

    def get(self):
        '''
            fetch student by page
        '''
        return self 

@namespace.response(http.HTTPStatus.ACCEPTED, 'data updated')
@namespace.response(http.HTTPStatus.BAD_REQUEST, '{field_name} is missing in your request')
@namespace.route("/students/<uuid:id>/update")
class RegisterStudent(Resource):
    
    @namespace.expect(student_registration_model, 201)
    @namespace.doc("update student data")

    def patch(self):
        '''
            update student data
        '''
        return self 



@namespace.response(http.HTTPStatus.NOT_FOUND, "not found")
@namespace.response(http.HTTPStatus.ACCEPTED, "student data deleted successfully")
@namespace.route("/students/delete/<uuid:id>")
@namespace.param('id', 'The student id')
class FetchStudentById(Resource):
    
    @namespace.doc("delete student by id")

    def delete(self):
        '''
            delete student by id
        '''
        return self 