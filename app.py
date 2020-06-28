"""Main Driver file for our FLask App"""


from flask import Flask, request, jsonify, make_response, render_template
from flask_migrate import Migrate
from sqlalchemy_utils import database_exists, create_database
from services import student_services, studentclass_services
from model.base import db

app = Flask(__name__)


def create_app(config):
    """Creates all configuration for our flask app"""
    # Init app

    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    #migrate = Migrate(app, db)
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.app_context():
        db.create_all()
        db.session.commit()
    return app


@app.route('/', methods=['GET'])
def home():
    """Render Home page for Students"""
    return render_template("index.html")


@app.route('/student', methods=['GET'])
def student_info():
    """Returns all students and student with specific ID"""
    student_id = request.args.get('id')
    if student_id:
        return student_services.get_student(student_id)
    return student_services.get_all_students()


@app.route('/student', methods=['POST'])
def student_add():
    """Add Student"""
    if request.content_type.startswith('application/json'):
        req_data = request.get_json()
        name = req_data['name']
        class_id = None
        if "class_id" in req_data:
            if req_data['class_id'] == "":
                class_id = None
            else:
                class_id = req_data['class_id']
        return student_services.add_student(name, class_id)
    return "Content type not valid"


@app.route('/student', methods=['PUT'])
def student_update():
    """Update Student"""
    if request.content_type.startswith('application/json'):
        req_data = request.get_json()
        student_id = req_data['id']
        if "name" in req_data:
            if req_data['name'] == "":
                name = None
            else:
                name = req_data['name']
        else:
            name = None
        if "class_id" in req_data:
            if req_data['class_id'] == "":
                class_id = None
            else:
                class_id = req_data['class_id']
        else:
            class_id = None
        print("CLASS - " + str(class_id))
        return student_services.update_student(student_id, name, class_id)
    return "Content type not valid"


@app.route('/student', methods=['DELETE'])
def student_delete():
    """Delete Student"""
    student_id = request.args.get('id')
    return student_services.delete_student(student_id)


@app.route('/class', methods=['GET'])
def class_info():
    """Get all the classes and Class by ID"""
    class_id = request.args.get('id')
    if class_id:
        return studentclass_services.get_class(class_id)
    return studentclass_services.get_all_class()


@app.route('/class', methods=['POST'])
def class_add():
    """Add Class"""
    if request.content_type.startswith('application/json'):
        req_data = request.get_json()
        name = req_data['name']
        if "class_leader" in req_data:
            if req_data['class_leader'] == "":
                class_leader = None
            else:
                class_leader = req_data['class_leader']
        else:
            class_leader = None
        return studentclass_services.add_class(name, class_leader)
    return "Content type not valid"


@app.route('/class', methods=['PUT'])
def class_update():
    """Update Student"""
    if request.content_type.startswith('application/json'):
        req_data = request.get_json()
        class_id = req_data['id']
        if "name" in req_data:
            if req_data['name'] == "":
                class_name = None
            else:
                class_name = req_data['name']
        else:
            class_name = None
        if "class_leader" in req_data:
            if req_data['class_leader'] == "":
                class_leader = None
            else:
                class_leader = req_data['class_leader']
        else:
            class_leader = None
        return studentclass_services.update_class(class_id, class_name, class_leader)
    return "Content type not valid"


@app.route('/class', methods=['DELETE'])
def class_delete():
    """Delete Student"""
    class_id = request.args.get('id')
    return studentclass_services.delete_class(class_id)


@app.errorhandler(404)
def not_found():
    """Not FOund page Function"""
    return make_response(jsonify({'error': 'Not found'}), 404)


# Run Server
if __name__ == "__main__":
    app = create_app('config.ProductionConfig')
    app.run(debug=True, host="0.0.0.0", port=5000)
