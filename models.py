from FlaskBasicAppWithConfig import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CourseName = db.Column(db.String(80), unique=True, nullable=False)
    CourseStartDate = db.Column(db.DateTime(120), nullable=False)

    def __repr__(self):
        return '<Course %r>' % self.CourseName