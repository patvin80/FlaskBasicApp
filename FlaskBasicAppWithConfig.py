from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from config import ProductionConfig, DevelopmentConfig
import os

app = Flask(__name__)
if (os.getenv("DEBUG", "True") == "True"):
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

db = SQLAlchemy(app)

##########################
# Models are now moved to a different file
##########################
from models import *

db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World Debugging'

@app.route('/insert/<coursename>')
def insert_course(coursename):
    c = Course(CourseName = coursename, CourseStartDate = date.today())
    db.session.add(c)
    db.session.commit()
    return "{0} successfully added with id {1}".format(coursename , c.id)

@app.route('/courses')
def list_courses():
    list_courses = Course.query.all()
    result = ''
    for course in list_courses:
        result = result + course.CourseName + " || "
    return result

@app.route('/courses/<id>')
def list_course(id):
    one_course = Course.query.filter_by(id=id).first()
    return "{0} starts on {1}".format(one_course.CourseName , one_course.CourseStartDate)

def create_app():
    if (os.getenv("DEBUG", "True") == "True"):
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)
    db.init_app(app)
    db.create_all()
    return app;

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=8080)
