import os
import functools
from flask import *
from flask import render_template
from app.models.model1 import *
from flask import current_app
from app.extensions import db
import bcrypt 
from werkzeug.utils import secure_filename
from flask_login import logout_user, login_user, login_required, current_user


auth_bp = Blueprint('auth',__name__)


#?creation of admin one time
# @auth_bp.route('/create_admin')
# def create_admin():
#     from app.extensions import db  # Make sure db is imported correctly
#     import bcrypt

#     # Admin credentials
#     username = 'admin@gmail.com'
#     plaintext_password = 'admin123'
#     hashed_password = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

#     # Create admin user
#     admin_user = Login(username=username, password=hashed_password, user_type='admin')
#     db.session.add(admin_user)
#     db.session.commit()

#     return 'Admin user created successfully with username: admin@gmail.com and password: admin123'

from flask import make_response
from functools import wraps

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response
    return no_cache


def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return 'login not success'
        return func()
    return secure_function





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
            
            #?check the hashed password and return true or false
            is_valid_password = bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8'))

            #? check if username and hashed password is correct
            if user and is_valid_password :
                #? check if the user is admin
                if user.user_type == 'admin':
                    session['lid'] = user.logid
                    return redirect(url_for('auth.adminDash'))
                
                #? check if the user is warden 
                elif user.user_type == 'warden':
                    if user.warden_info.status != 'active':
                        return f'Login blocked , status {user.warden_info.status}',403
                    else:
                        session['lid'] = user.logid
                        return 'login successful',200
                #? check if the user is student 
                elif  user.user_type =='student':
                    if user.student_info.status != 'active':
                        return f'Login blocked , status {user.student_info.status}',403
                    else:
                        session['lid'] = user.logid
                        return 'login successful',200
            #? check if student status is acitve or not  
            else :
                return 'invalid username or password',401
            
    except ValueError as ve:
        return{'error':str(ve)},401

#? ------------student registration route----------------

@auth_bp.route('/registerLinkStudent',methods=['POST','GET'])
def registerLinkStudent():
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

            #? plain text password is hashed using bcrypt function hashpw()
            password_hash =  bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

            
            new_user_login = Login(username=email,password=password_hash,user_type='student')

            db.session.add(new_user_login)
            db.session.commit()

            new_user = Students(full_name=fullname,email=email,phone_number=phone,date_of_birth=dob,address=address,admission_date=admission_date,emergency_contact_name=em_contact_name,emergency_contact_phone=em_contact_number,guardian_name=guardian_name,photo_url=url,logid=new_user_login.logid)

            db.session.add(new_user)
            db.session.commit()

            return 'user added to login table'

    except ValueError as ve:
        return {'error':str(ve)},401
    


# #? ------------warden home route----------------

@auth_bp.route('/registerLinkWarden',methods=['POST','GET'])
def registerLinkWarden():
    return render_template('warden-reg-form.html')


# #? ------------student registration function----------------

@auth_bp.route('/registrationWardens',methods=['POST'])
def registrationWardens():
    try:

        if request.method=='POST':
            fullname = request.form['full_name']
            email = request.form['email']
            phone = request.form['phone_number']
            dob = request.form['date_of_birth']
            address = request.form['address']
            resume_file = request.files.get('resume')
            url = request.form['photo_url']
            password = request.form['password']

            #? the resume file is stored in to the system folder and file name is stored in the db
            upload_folder = current_app.config['UPLOAD_FOLDER'] 
            filename = None    
            if resume_file and resume_file.filename != '':     
                filename = secure_filename(resume_file.filename)
                file_path = os.path.join(upload_folder, filename)
                resume_file.save(file_path)
            else:
                filename = 'no_resume_uploaded.pdf'     



            #? plain text password is hashed using bcrypt function hashpw()
            password_hash =  bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

            
            new_user_login = Login(username=email,password=password_hash,user_type='warden')

            db.session.add(new_user_login)
            db.session.commit()

            new_user = Wardens(full_name=fullname,email=email,phone_number=phone,date_of_birth=dob,address=address,resume=filename,photo_url=url,logid=new_user_login.logid)

            db.session.add(new_user)
            db.session.commit()

            return 'user added to login table'

    except ValueError as ve:
        return {'error':str(ve)},401
    
#? ------------admin dashboard----------------
@auth_bp.route('/adminDash',methods=['GET','POST'])
@login_required
@nocache
def adminDash():
    return render_template('admin-dashboard.html')

