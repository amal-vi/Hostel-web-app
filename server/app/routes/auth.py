from flask import *
from flask import render_template
from app.models.model1 import *
from app.extensions import db
auth_bp = Blueprint('auth',__name__)


#? ------------login route----------------

@auth_bp.route('/',methods=['POST','GET'])
def main():
    return render_template('login.html')

#? ------------login function----------------

@auth_bp.route('/login',methods=['POST'])
def login():
    try:
        if request.method == 'POST':
            username=request.form['username']
            password=request.form['password']

            #? get the entered username and password from the table
            user = db.session.query(Login).filter_by(username=username).first()
            passkey = db.session.query(Login).filter_by(password=password).first()


            #? check if username and password is correct
            if user and passkey :
                #? check if the user is student 
                if  not user.user_type =='student':
                    return 'Student profile not found',403
                #? check if student status is acitve or not  
                if user.student_info.status != 'active':
                    return 'Login blocked , status {user.student_info.status}',403
                else:
                    return 'login successful',200
            else :
                return 'invalid username or password',401
    except ValueError as ve:
        return{'error:str(ve)'},401

#? ------------student registration route----------------

@auth_bp.route('/registerLink',methods=['POST','GET'])
def registerLink():
    return render_template('student-reg-form.html')

#? ------------student registration function----------------


@auth_bp.route('/registrationStudents',methods=['POST'])
def registrationStudents():
    try:
        if request.method=='POST':
            fullname = request.form['full_name']
            email = request.form['email']
            phone = request.form['phone_number']
            dob = request.form['date_of_birth']
            address = request.form['address']
            admission_date = request.form['admission_date']
            em_contact_name = request.form['emergency_contact_name']
            em_contact_number = request.form['emergency_contact_phone']
            guardian_name = request.form['guardian_name']
            url = request.form['photo_url']
            password = request.form['password']

            new_user = Students(full_name=fullname,email=email,phone_number=phone,date_of_birth=dob,address=address,admission_date=admission_date,emergency_contact_name=em_contact_name,emergency_contact_phone=em_contact_number,guardian_name=guardian_name,photo_url=url,password_hash=password)
            
            new_user_login = Login(username=email,password=password)

            db.session.add(new_user_login)
            db.session.commit()

            new_user = Students(full_name=fullname,email=email,phone_number=phone,date_of_birth=dob,address=address,admission_date=admission_date,emergency_contact_name=em_contact_name,emergency_contact_phone=em_contact_number,guardian_name=guardian_name,photo_url=url,password_hash=password,logid=new_user_login.logid)

            db.session.add(new_user)
            db.session.commit()

            return 'user added to login table'

    except ValueError as ve:
        return {'error:str(ve)'},401
    


#? ------------warden home route----------------

@auth_bp.route('/wardenDashboard',methods=['post','get'])
def wardenDashboard():
    return render_template('')


