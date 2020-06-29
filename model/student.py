"""Module for Student database"""

from .base import db



class Student(db.Model):
    """Class for student"""
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('studentclass.id'), nullable=True)
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
            'class_id': self.class_id,
            'created_on': self.created_on,
            'updated_on': self.updated_on,
        }
