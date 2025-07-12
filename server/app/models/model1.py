from app.extensions import db

class Login(db.Model):
    __tablename__ = 'login_info' 
    logid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    user_type = db.Column(db.Enum('student', 'warden', 'admin'),nullable=False,default='student')

    student_info = db.relationship('Students', back_populates='login', uselist=False)

class Students(db.Model):
    __tablename__ = 'student_info'
    student_id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),nullable=False)
    phone_number = db.Column(db.String(150),nullable=False)
    date_of_birth = db.Column(db.Date,nullable=False)
    address = db.Column(db.Text,nullable=False)
    admission_date = db.Column(db.Date,nullable=False)
    room_number = db.Column(db.String(150),nullable=False,default='pending')
    emergency_contact_name = db.Column(db.String(150),nullable=False)
    emergency_contact_phone = db.Column(db.String(150),nullable=False)
    guardian_name = db.Column(db.String(150),nullable=False)
    photo_url = db.Column(db.String(150),nullable=False)
    password_hash = db.Column(db.String(150),nullable=False)
    status = db.Column(db.Enum('inactive','active','pending'),nullable=False,default='pending')
    user_type = db.Column(db.String(150),nullable=False,default='student')
    logid = db.Column(db.Integer,db.ForeignKey('login_info.logid'),nullable=False)

    login = db.relationship('Login', back_populates='student_info')

class Warden(db.Model):
    __tablename__ = 'warden_info'
    




    