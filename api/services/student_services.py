from pydoc import cli

from grpc import StatusCode
from api.model import  Students
from http import client
from flask import jsonify
from api.services.extensions_services import db
from sqlalchemy.exc import DataError
from api.services.serializer_service import student_serializer


#   service to add students to the database

def admin_add_student_service(student_data):
    #   setup field validation via try keyword
    try:

        student_first_name = student_data["first_name"]
        student_last_name = student_data["last_name"]
        student_matrict_no = student_data["matric_no"]
        student_department = student_data["department"]
        student_level = student_data["level"]
        student_email = student_data["email"]

    except Exception as KeyError:
        return jsonify(status='failed', message = f'{KeyError.args[0]} field is missing in your request'), client.BAD_REQUEST
    

    check_student_email = Students.query.filter_by(email = student_email).first()
    check_student_matric = Students.query.filter_by(matric_no = student_matrict_no).first()

    if check_student_email:
        return jsonify(status='failed', message = "existing email"), client.FORBIDDEN
    
    if check_student_matric:
        return jsonify(status='failed', message = "existing matric no"), client.FORBIDDEN


    student = Students(

        first_name = student_first_name,
        last_name = student_last_name,
        email = student_email,
        department = student_department,
        level = student_level,
        matric_no = student_matrict_no

    )

   
    #   save the data  in the database
    db.session.add(student)
    db.session.commit()

  
    return jsonify(
        status= "success",
        message = "student registered successfully"
        ), client.CREATED


#   service to fetch students
def admin_fetch_student_by_id(student_uuid):

    try:

        student = Students.query.filter_by(id=student_uuid).first()

    except DataError:
        return jsonify(status="failed", message = "invalid id type"), client.FORBIDDEN

    if not student:
        return jsonify(status="failed", message = "invalid id"), client.NOT_FOUND
    
    return jsonify(
        status = "success",
        first_name = student.first_name,
        last_name = student.last_name,
        matric_no = student.matric_no,
        level = student.level,
        department = student.department,
        email = student.email,
        id = student.id
        ), client.ACCEPTED

#   service to fetch all students students
def admin_fetch_all_students(page):
    
    #   query all students
    #   paginate by 10 pages

    all_students_per_page = Students.query.paginate(page=page, per_page=10).items

    #   serialize students
    serialized_students = [*map(student_serializer, all_students_per_page)]


    return jsonify(
        status = "success",
        students = serialized_students,
        page = page
        ), client.OK


#   service to update a student resource
def admin_update_student(student_uuid, student_updated_data):

    fetch_student = Students.query.get_or_404(student_uuid)

    try:
        fetch_student.first_name = student_updated_data["first_name"]
        fetch_student.last_name = student_updated_data["last_name"]
        fetch_student.email = student_updated_data["email"]
        fetch_student.matric_no = student_updated_data["matric_no"]
        fetch_student.level = student_updated_data["level"]
        fetch_student.department = student_updated_data["department"]
    
    except Exception as KeyError:
        return jsonify(status='failed', message = f'{KeyError.args[0]} field is missing in your request'), client.BAD_REQUEST

    #   effect the change in the database
    db.session.commit()

    return jsonify(
        status= "success",
        message = "data updated",
    ), client.ACCEPTED

#   service to delete the student resource

def admin_delete_student_resource(student_uuid):

    fetch_student = Students.query.get_or_404(student_uuid)
    
    #   delete the student's data
    db.session.delete(fetch_student)

    #   effect the change in the database
    db.session.commit()
    return jsonify(
            status = "success",
            message = "student data deleted successfully"
        ), client.ACCEPTED