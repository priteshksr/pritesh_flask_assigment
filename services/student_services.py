from model.student import Student
from flask import jsonify
from model.base import db


def get_student(student_id):
    try:
        student_by_id = Student.query.filter_by(id=student_id).first()
        return jsonify(student_by_id=student_by_id.serialize)
    except Exception as e:
        db.session.rollback()
        raise e


def get_all_students():
    try:
        students = Student.query.all()
        return jsonify(students=[student.serialize for student in students])
    except Exception as e:
        db.session.rollback()
        raise e


def add_student(student_name, class_id):
    try:
        student = Student(name=student_name)
        if class_id:
            student.class_id = class_id
        db.session.add(student)
        db.session.commit()
        return jsonify(student=student.serialize)
    except Exception as e:
        db.session.rollback()
        raise e


def delete_student(student_id):
    try:
        student = Student.query.filter_by(id=student_id).first()
        db.session.delete(student)
        db.session.commit()
        return 'Removed Student with id %s' % student_id
    except Exception as e:
        db.session.rollback()
        raise e


def update_student(student_id, student_name, class_id):
    try:
        student = Student.query.filter_by(id=student_id).first()
        if student_name:
            student.name = student_name
        if class_id:
            student.class_id = class_id
        print(student.class_id)
        db.session.commit()
        return jsonify(student=student.serialize)

    except Exception as e:
        db.session.rollback()
        raise e
