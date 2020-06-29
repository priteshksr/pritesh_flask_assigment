"""Module for class database"""

from .base import db


class StudentClass(db.Model):
    """class defined for StudentClass"""
    __tablename__ = 'studentclass'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    class_leader = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=True)
    created_on = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_on = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    def __init__(self, name):
        """constructor function"""
        self.name = name

    @property
    def serialize(self):
        """function to serialize the output"""
        return {
            'id': self.id,
            'name': self.name,
            'class_leader': self.class_leader,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
        }
