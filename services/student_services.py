"""This module is for all services for student_class"""

from flask import jsonify
from model.student import Student
from model.base import db


def get_student(student_id):
    """function to get student by ID"""
    try:
        student_by_id = Student.query.filter_by(id=student_id).first()
        return jsonify(student_by_id=student_by_id.serialize)
    except Exception as error:
        db.session.rollback()
        raise error


def get_all_students():
    """function to get all students"""
    try:
        students = Student.query.all()
        return jsonify(students=[student.serialize for student in students])
    except Exception as error:
        db.session.rollback()
        raise error


def add_student(student_name, class_id):
    """function to add student"""
    try:
        student = Student(name=student_name)
        if class_id:
            student.class_id = class_id
        db.session.add(student)
        db.session.commit()
        return jsonify(student=student.serialize)
    except Exception as error:
        db.session.rollback()
        raise error


def delete_student(student_id):
    """function to delete student"""
    try:
        student = Student.query.filter_by(id=student_id).first()
        db.session.delete(student)
        db.session.commit()
        return 'Removed Student with id %s' % student_id
    except Exception as error:
        db.session.rollback()
        raise error


def update_student(student_id, student_name, class_id):
    """function to update student"""
    try:
        student = Student.query.filter_by(id=student_id).first()
        if student_name:
            student.name = student_name
        if class_id:
            student.class_id = class_id
        print(student.class_id)
        db.session.commit()
        return jsonify(student=student.serialize)

    except Exception as error:
        db.session.rollback()
        raise error
