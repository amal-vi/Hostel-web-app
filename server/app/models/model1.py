from app.extensions import db

class Login(db.Model):
    __tablename__ = 'login_info' 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)


# class Students(db.Model):
#     __tablenaem__ = 'student_info'
#     id = db.Column(db.Integer,primary_key=True)
#     user_type = db.column(db.String(150),nullable=False,default='student')

    