from flask_jwt_extended import create_access_token
from flask import jsonify, g
from api.model import Admins
from api.services.extensions_services import db
from http import client
from sqlalchemy.exc import IntegrityError




#   service to handle the admin registration request

def admin_registration_service(data):

    #   setup field validation via try keyword
    try:

        admin_first_name = data["first_name"]
        admin_last_name = data["last_name"]
        admin_email = data["email"]
        admin_password = data["password"]

    except Exception as KeyError:
        return jsonify(status='failed', message = f'{KeyError.args[0]} field is missing in your request'), client.BAD_REQUEST

    #   if no error, setup the admin

    
    admin = Admins(

        first_name = admin_first_name,
        last_name = admin_last_name,
        email = admin_email
        
    )
    
    
    #   store the password hash
    admin.hash_password(admin_password)

    try:
        #   save the data  in the database
        db.session.add(admin)
        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        return jsonify(status='failed', message = "admin credentials exists already"), client.FORBIDDEN
    

    return jsonify(
        status= "success",
        message = "admin registered successfully"
        ), client.CREATED


#   service to login the admin

def admin_login_service(data):

    #   setup field validation via try keyword
    try:

        admin_email = data["email"]
        admin_password = data["password"]

    except Exception as KeyError:
        return jsonify(status='failed', message = f'{KeyError.args[0]} field is missing in your request'), client.BAD_REQUEST

    fetched_admin = Admins.query.filter_by(email=admin_email).first()

    #   check for  invalid email or password
    if not fetched_admin or not fetched_admin.verify_password(admin_password):
        return jsonify(status="failed", message="invalid credentials"), client.NOT_FOUND
    
    #   create access token
    g.user = fetched_admin
    access_token = create_access_token(identity=g.user.email)
    return jsonify(status="success", message="logged in successfully", access_token=access_token), client.ACCEPTED


