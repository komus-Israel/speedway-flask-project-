#   student serializer

def student_serializer(student):
    return dict(

        id = student.id,
        first_name = student.first_name,
        last_name = student.last_name,
        matric_no = student.matric_no,
        level = student.level,
        department = student.department,
        email = student.email,
        
        )