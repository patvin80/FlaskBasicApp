from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from config import ProductionConfig, DevelopmentConfig

app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] =  'sqlite:///test.db'
app.config["SECRET_KEY"] = "ABCDE"
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CourseName = db.Column(db.String(80), unique=True, nullable=False)
    CourseStartDate = db.Column(db.DateTime(120), nullable=False)

    def __repr__(self):
        return '<Course %r>' % self.CourseName

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


if __name__ == '__main__':
    db.create_all()
    app.run()
