from app import create_app
from flask import json, Flask
import pytest
from model.base import db
from sqlalchemy_utils import database_exists, create_database

TEST_STUDENT = None
TEST_CLASS = None


@pytest.fixture()
def app():
    app = Flask(__name__)
    app = create_app('config.TestingConfig')
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


def test_studentpost(app):
    global TEST_STUDENT
    response = app.test_client().post(
        '/student',
        data=json.dumps({'name': "Pritesh", 'class_id': ""}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    data = data["student"]
    TEST_STUDENT = data['id']
    assert response.status_code == 200
    assert data['name'] == "Pritesh"
    if data['class_id'] is None:
        assert True
    else:
        assert False


def test_classpost(app):
    global TEST_CLASS
    response = app.test_client().post(
        '/class',
        data=json.dumps({'name': "Class V", 'class_leader': ""}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    data = data["student_class"]
    TEST_CLASS = data['id']
    assert response.status_code == 200
    # assert data['id'] == 1
    assert data['name'] == "Class V"
    if data['class_leader'] is None:
        assert True
    else:
        assert False


def test_studentput(app):
    global TEST_STUDENT
    response = app.test_client().put(
        '/student',
        data=json.dumps({'id': TEST_STUDENT, 'name': "Prit", 'class_id': ""}),
        content_type='application/json',
    )

    data = response.get_data(as_text=True)
    assert response.status_code == 200


def test_classput(app):
    global TEST_CLASS
    response = app.test_client().put(
        '/class',
        data=json.dumps({'id': TEST_CLASS, 'name': "Class VI", 'class_leader': ""}),
        content_type='application/json',
    )

    data = response.get_data(as_text=True)

    assert response.status_code == 200


def test_studentsget(app):
    response = app.test_client().get(
        '/student'
    )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data['students']) > 0


def test_studentget(app):
    global TEST_STUDENT
    response = app.test_client().get(
        '/student?id=' + str(TEST_STUDENT)
    )
    data = json.loads(response.get_data(as_text=True))
    data = data['student_by_id']
    assert response.status_code == 200
    assert data['name'] == 'Prit'


def test_classesget(app):
    global TEST_CLASS
    response = app.test_client().get(
        '/class'
    )
    data = json.loads(response.get_data(as_text=True))
    data = data['all_class']
    assert response.status_code == 200
    assert len(data) > 0


def test_classget(app):
    global TEST_CLASS
    response = app.test_client().get(
        '/class?id=' + str(TEST_CLASS)
    )
    data = json.loads(response.get_data(as_text=True))
    data = data['class_by_id']
    assert response.status_code == 200
    assert data['name'] == 'Class VI'


def test_studentdelete(app):
    global TEST_STUDENT
    response = app.test_client().delete(
        '/student?id=' + str(TEST_STUDENT)
    )
    data = response.get_data(as_text=True)
    assert response.status_code == 200


def test_classdelete(app):
    global TEST_CLASS
    response = app.test_client().delete(
        '/class?id=' + str(TEST_CLASS)
    )
    data = response.get_data(as_text=True)
    assert response.status_code == 200
