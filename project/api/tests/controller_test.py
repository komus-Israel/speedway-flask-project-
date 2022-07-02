from os import access
from urllib import response
from numpy import deprecate
import pytest
from api import create_app, db
import http
import json
from flask_jwt_extended import create_access_token

app = create_app("test")




client = app.test_client()
json_content_type = "application/json"


def test_admin_registration_route():

    with app.app_context():


        #   create db
        db.create_all()
        
        #   failed cases

        admin_data = dict( first_name = "Israel")
        response = client.post("/admin/register", data = json.dumps(admin_data), content_type = json_content_type )
        
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

        #   success case
        admin_data = dict(first_name = "Israel", last_name = "Komolehin", email = "test@gmail.com", password = "access")
        response = client.post("/admin/register", data = json.dumps(admin_data), content_type = json_content_type)
        assert response.status_code == http.HTTPStatus.CREATED

        #   failed case for re registering same admin email
        response = client.post("/admin/register", data = json.dumps(admin_data), content_type = json_content_type)
        assert response.status_code == http.HTTPStatus.FORBIDDEN

        #   empty the database
        db.drop_all()
        db.session.commit()



'''def test_admin_login_route():

    
    
    with app.app_context():

        #   create db
        db.create_all()

        #   create admin
        admin_data = dict(first_name = "Israel", last_name = "Komolehin", email = "test@gmail.com", password = "access")
        data = client.post("/admin/register", data = json.dumps(admin_data), content_type = json_content_type)
        assert data.status_code == http.HTTPStatus.CREATED

        

        login_data = dict(email = "test@gmail.com", password = "access")
        data = client.post("/admin/login", data = json.dumps(login_data), content_type = json_content_type)
        #assert data.status_code == http.HTTPStatus.CREATED
        

        #   empty the database
        db.drop_all()
        db.session.commit()'''


def test_admin_add_new_student():

    with app.app_context():

        db.drop_all()
        #   create db
        db.create_all()

        #   create access token
        access_token = create_access_token("admin@gmail.com")

        #   create authorization header

        header = {
            "Authorization": 'Bearer {}'.format(access_token)
            
        }

        #   incomplete student data
        student_data = dict(
            first_name = "tim", last_name = "Kom",
            email = "tim@testmail.com", 
        )

        response = client.post("/admin/students/new", data = json.dumps(student_data), headers = header, content_type = json_content_type)
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

        #   complete student data
        student_data = dict(
            first_name = "tim", last_name = "Kom",
            email = "tim@testmail.com", matric_no = "12332scsdv",
            level = "400", department = "biochem"
        )

        response = client.post("/admin/students/new", data = json.dumps(student_data), headers = header, content_type = json_content_type)
        assert response.status_code == http.HTTPStatus.CREATED
        
        

        #   failed registration for existing email

        student_data = dict(
            first_name = "tim", last_name = "Kom",
            email = "tim@testmail.com", matric_no = "12332scs",
            level = "400", department = "biochem"
        )

        response = client.post("/admin/students/new", headers = header, data = json.dumps(student_data), content_type = json_content_type)
        assert response.status_code == http.HTTPStatus.FORBIDDEN
        

        #   failed reg for exisiting matric no
        student_data = dict(
            first_name = "tim", last_name = "Kom",
            email = "tim@testmail2.com", matric_no = "12332scsdv",
            level = "400", department = "biochem"
        )

        response = client.post("/admin/students/new", data = json.dumps(student_data), headers = header, content_type = json_content_type)
        assert response.status_code == http.HTTPStatus.FORBIDDEN



        

def test_get_admin():

    with app.app_context():
        access_token = create_access_token("admin@gmail.com")
        db.create_all()
        header = {
            "Authorization": 'Bearer {}'.format(access_token)
        }
        response = client.get("/admin/students/get/59bb2e6f-5678-4645-883e-1a907735ddba", headers = header)
        assert response.status_code == http.HTTPStatus.NOT_FOUND