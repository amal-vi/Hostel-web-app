from flask import *
from flask import render_template
from app.models.model1 import Login
from app.extensions import db
auth_bp = Blueprint('auth',__name__)

@auth_bp.route('/',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']

        new_user = Login(username=username,password=password)
        db.session.add(new_user)
        db.session.commit()

        return 'user added to login table'
    
    return render_template('login.html')    

@auth_bp.route('/register',methods=['post','get'])
def registerLink():
    return render_template('student-reg-form.html')

# @auth_bp.route('/students_registration',methods=['post'])
# def registrationStudents():
#     if request.method=='POST':
        

