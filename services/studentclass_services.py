from model.studentclass import StudentClass
from flask import Flask, request, jsonify, make_response
from model.base import db


def get_class(class_id):
    try:
        class_by_id = StudentClass.query.filter_by(id=class_id).first()
        return jsonify(class_by_id=class_by_id.serialize)
    except Exception as e:
        db.session.rollback()
        raise e


def get_all_class():
    try:
        all_class = StudentClass.query.all()
        return jsonify(all_class=[cla.serialize for cla in all_class])
    except Exception as e:
        db.session.rollback()
        raise e


def add_class(class_name, class_leader):
    try:
        student_class = StudentClass(name=class_name)
        student_class.class_leader = class_leader
        db.session.add(student_class)
        db.session.commit()
        return jsonify(student_class=student_class.serialize)
    except Exception as e:
        db.session.rollback()
        raise e


def delete_class(class_id):
    try:
        deleted_class = StudentClass.query.filter_by(id=class_id).first()
        db.session.delete(deleted_class)
        db.session.commit()
        return 'Removed Class with id %s' % class_id
    except Exception as e:
        db.session.rollback()
        raise e


def update_class(class_id, class_name, class_leader):
    try:
        updated_class = StudentClass.query.filter_by(id=class_id).first()
        if class_name:
            updated_class.name = class_name
        if class_leader:
            updated_class.class_leader = class_leader
        db.session.add(updated_class)
        db.session.commit()
        return jsonify(Class=updated_class.serialize)

    except Exception as e:
        db.session.rollback()
        raise e
