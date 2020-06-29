"""This module is for all services for student_class"""

from flask import jsonify
from model.studentclass import StudentClass
from model.base import db


def get_class(class_id):
    """function to get class"""
    try:
        class_by_id = StudentClass.query.filter_by(id=class_id).first()
        return jsonify(class_by_id=class_by_id.serialize)
    except Exception as error:
        db.session.rollback()
        raise error


def get_all_class():
    """function to get all classes"""
    try:
        all_class = StudentClass.query.all()
        return jsonify(all_class=[cla.serialize for cla in all_class])
    except Exception as error:
        db.session.rollback()
        raise error


def add_class(class_name, class_leader):
    """function to add class"""
    try:
        student_class = StudentClass(name=class_name)
        student_class.class_leader = class_leader
        db.session.add(student_class)
        db.session.commit()
        return jsonify(student_class=student_class.serialize)
    except Exception as error:
        db.session.rollback()
        raise error


def delete_class(class_id):
    """function to delete class"""
    try:
        deleted_class = StudentClass.query.filter_by(id=class_id).first()
        db.session.delete(deleted_class)
        db.session.commit()
        return 'Removed Class with id %s' % class_id
    except Exception as error:
        db.session.rollback()
        raise error


def update_class(class_id, class_name, class_leader):
    """function to update class"""
    try:
        updated_class = StudentClass.query.filter_by(id=class_id).first()
        if class_name:
            updated_class.name = class_name
        if class_leader:
            updated_class.class_leader = class_leader
        db.session.add(updated_class)
        db.session.commit()
        return jsonify(Class=updated_class.serialize)

    except Exception as error:
        db.session.rollback()
        raise error
